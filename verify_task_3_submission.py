import json
import argparse

TASK_QUESTIONS = {
    0: {
        "Question": "What type of procedure is the image taken from?",
        "Required": False,
    },
    1: {
        "Question": "Have all polyps been removed?",
        "Required": False,
    },
    2: {
        "Question": "Is this finding easy to detect?",
        "Required": False,
    },
    3: {
        "Question": "Is there a green/black box artefact?",
        "Required": False,
    },
    4: {
        "Question": "Is there text?",
        "Required": False,
    },
    5: {
        "Question": "What color is the abnormality?",
        "Required": False,
    },
    6: {
        "Question": "What color is the anatomical landmark?",
        "Required": False,
    },
    7: {
        "Question": "How many findings are present?",
        "Required": False,
    },
    8: {
        "Question": "How many polyps are in the image?",
        "Required": False,
    },
    9: {
        "Question": "How many instrumnets are in the image?",
        "Required": False,
    },
    10: {
        "Question": "Where in the image is the abnormality?",
        "Required": False,
    },
    11: {
        "Question": "Where in the image is the instrument?",
        "Required": False,
    },
    12: {
        "Question": "Are there any abnormalities in the image?",
        "Required": False,
    },
    13: {
        "Question": "Are there any anatomical landmarks in the image?",
        "Required": False,
    },
    14: {
        "Question": "Are there any instruments in the image?",
        "Required": False,
    },
    15: {
        "Question": "Where in the image is the anatomical landmark?",
        "Required": False,
    },
    16: {
        "Question": "What is the size of the polyp?",
        "Required": False,
    },
    17: {
        "Question": "What type of polyp is present?",
        "Required": False,
    },
    18: {
        "Question": "Where exactly in the image is the polyp located?",
        "Required": True,
    },
    19: {
        "Question": "Where exactly in the image is the instrument located?",
        "Required": True,
    },
}

def read_image_ids(image_ids_file):
    with open(image_ids_file, "r") as f:
        image_ids = [line.strip() for line in f if line.strip()]
    return image_ids


def check_predictions_file(predictions_file, image_ids):
    with open(predictions_file, "r") as f:
        predictions_data = json.load(f)

    for image_id in image_ids:
        if image_id not in image_ids:
            print(f"Invalid image_id: {image_id}")
            return False

        question_ids = list(TASK_QUESTIONS.keys())

        for prediction in predictions_data[image_id]:
            # Check if the prediction has the correct keys
            if (
                "QuestionID" not in prediction
                or "Question" not in prediction
                or "Answer" not in prediction
            ):
                print(
                    "Each prediction must contain 'QuestionID', 'Question', and 'Answer' keys."
                )
                return False

            # Check if the question_id and image_id are valid
            question_id = prediction["QuestionID"]

            if question_id not in question_ids:
                print(f"{image_id} contains the invalid question_id: {question_id}")
                return False

            # Remove the processed question_id from the set
            question_ids.remove(question_id)

        for question_id, question_dict in TASK_QUESTIONS.items():
            if question_id in question_ids and not question_dict["Required"]:
                question_ids.remove(question_id)

        # Check if all questions have been answered
        if question_ids:
            print(f"The following question IDs are missing from {image_id} in the prediction file:")
            print(sorted(question_ids))
            return False

        print(
            "The prediction file has the correct format and contains answers for all questions."
        )
        return True


def main():
    parser = argparse.ArgumentParser(
        description="Check the prediction file format and completeness."
    )
    parser.add_argument(
        "-p",
        "--submission-predictions",
        type=str,
        default="sample_submission.json",
        help="Prediction JSON file path.",
    )
    parser.add_argument(
        "-i",
        "--image_ids_file",
        type=str,
        default="test_image_ids.txt",
        help="Text file containing image IDs.",
    )
    args = parser.parse_args()

    image_ids = read_image_ids(args.image_ids_file)

    check_predictions_file(args.submission_predictions, image_ids)


if __name__ == "__main__":
    main()
