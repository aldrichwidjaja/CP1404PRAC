def scoretosubject(score_values):
    subject_scores = []
    number_of_subjects = len(score_values[0])
    for _ in range(number_of_subjects):
        scores_for_one_subject = []
        for scores in score_values:
            scores_for_one_subject.append(scores.pop(0))
        subject_scores.append(scores_for_one_subject)
    return subject_scores

def data_subject(scores_by_subject, subject_names):
    for i, scoresper_subject in enumerate(scores_by_subject):
        print(subject_names[i], "Scores:")
        for score in scoresper_subject:
            print("{:>2}".format(score))
        print("Max: {:3}".format(max(scoresper_subject)))
        print("Min: {:3}".format(min(scoresper_subject)))
        print("Avg: {:6.2f}\n".format(
            (sum(scoresper_subject) / len(scoresper_subject))))

def main():
    openscorefile = open("scores.csv")
    scorefile_data = openscorefile.readlines()
    studentsubject = scorefile_data[0].strip().split(",")
    scoredata_values = []

    for score_line in scorefile_data[1:]:
        score_strings = score_line.strip().split(",")
        score_numbers = [int(value) for value in score_strings]
        scoredata_values.append(score_numbers)
    openscorefile.close()
    scores_by_subject = scoretosubject(scoredata_values)
    data_subject(scores_by_subject, studentsubject)


main()