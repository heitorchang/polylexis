def parse(questionlines):
    questions = questionlines.splitlines()

    words_display = ""
    allans_table = ""

    for question in questions:
        question = question.strip()

        if len(question) > 0:
            all_prompts, all_answers = question.split("*")
            all_prompts = all_prompts.strip()
            all_answers = all_answers.strip()

            prompts = all_prompts.split("/")
            answers = all_answers.split("/")

            prompts_display = '["' + '", "'.join(prompts) + '"]'
            answers_display = '["' + '", "'.join(answers) + '"]'

            words_display += f"""
            {{
              prompt: {prompts_display},
              answer: {answers_display},
            }},
            """

            # prompt_no_underscore = prompt.replace("_", "").strip()

            allans_table += f"""
            <tr><td>{all_prompts}</td><td style="padding-left: 0.5em;">{all_answers}</td></tr>
            """
            
    return words_display, allans_table

