def iou(box1, box2):

    """

        Calculates the IoU between two boxes

    """

    # Unpack
    (box1_x1, box1_y1, box1_x2, box1_y2) = box1
    (box2_x1, box2_y1, box2_x2, box2_y2) = box2

    # Calculate intersection area
    xi1 = max(box1_x1, box2_x1)
    yi1 = max(box1_y1, box2_y1)
    xi2 = min(box1_x2, box2_x2)
    yi2 = min(box1_y2, box2_y2)
    inter_width = max(0, xi2 - xi1)
    inter_height = max(0, yi2 - yi1)
    inter_area = inter_width * inter_height

    # Calculate union area
    box1_area = (box1_x2 - box1_x1) * (box1_y2 - box1_y1)
    box2_area = (box2_x2 - box2_x1) * (box2_y2 - box2_y1)
    union_area = box1_area + box2_area - inter_area

    # Calculate IoU
    return (1.0 * inter_area) / union_area


def calculate_stats(ground_truth, predictions):

    """

    Returns object detection precision and recall values for a single frame and ground truth

    :param ground_truth: A list of (confidence: float, prediction: string, bbox: (4 integers))
    :param predictions: A list of (confidence: float, prediction: string, bbox: (4 integers))
    :return:
    """

    # True positive, false positive
    tp = 0
    fp = 0
    # Do not use the same ground truth object to justify two objects
    marked = [False] * len(ground_truth)

    for i in range(len(predictions)):
        found = False
        for j in range(len(ground_truth)):
            # Labels are the same
            if (not marked[j]) and (predictions[i][0] == ground_truth[j][0]):
                # Higher IoU than the threshold
                if iou(predictions[i][1], ground_truth[j][1]) > 0.5:
                    tp += 1
                    marked[j] = True
                    found = True
                    break
        # If prediction can not be in the ground truth, then it is false positive
        if not found:
            fp += 1
    if tp+fp != 0:
        precision = (1.0 * tp) / (tp + fp)
    else:
        precision = float('nan')

    if len(ground_truth) != 0:
        recall = (1.0 * tp) / len(ground_truth)
    else:
        recall = float('nan')

    return precision, recall
