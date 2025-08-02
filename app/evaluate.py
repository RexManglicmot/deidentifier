from sklearn.metrics import precision_score, recall_score, f1_score
from app.logger_config import logger


def evaluate_entities(true_entities, predicted_entities):
    """
    Function to using 3 metrics Precision, Recall, and F1 Score.

      Args:
        true_entities (list of dict): Ground truth, each dict must contain 'start', 'end', 'entity_type'
        predicted_entities (list of dict): Model output, same format.

    Returns:
        dict: Precision, Recall, F1 score

    """
    
    # Helper function to convert entity dictionaries into a set of tuples for easy comparison
    # This function is only used inside evaluate_entities, so we keep it nested
    # to limit its scope and avoid cluttering the module-level namespace.
    
    # Logging start
    logger.info("Starting evaluation of detected entities...")

    def spans_to_set(entity_list):

        # e here is each element in the entity list
        # # Convert list of entity dicts to a set of (start, end, type) tuples for easy comparison
        return set((e['start'], e['end'], e['entity_type']) for e in entity_list)

    # Convert both true and predicted entity lists into sets
    true_set = spans_to_set(true_entities)
    pred_set = spans_to_set(predicted_entities)

    # Compute the number of correct predictions (intersection of sets)
    true_positive = len(true_set & pred_set)

    # Compute false positives (predicted but not in true set)
    false_positive = len(pred_set - true_set)

    # Compute false negatives (missed detections from the true set)
    false_negative = len(true_set - pred_set)

    # Calculate precision: TP / (TP + FP)
    precision = true_positive / (true_positive + false_positive) if (true_positive + false_positive) else 0

    # Calculate recall: TP / (TP + FN)
    recall = true_positive / (true_positive + false_negative) if (true_positive + false_negative) else 0

    # Calculate F1 score: harmonic mean of precision and recall
    f1 = (2 * precision * recall) / (precision + recall) if (precision + recall) else 0

    # Logging end
    logger.info("Evaluation Complete")

    # Return metrics as a dictionary
    return {
        "precision": round(precision, 4),
        "recall": round(recall, 4),
        "f1_score": round(f1, 4)
    }

# COMPLETE
