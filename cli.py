from Database.queries import *

menu_options = {
    1: 'View problems by subject',
    2: 'View problems by submits between 2 number',
    3: 'View problems by difficulty between 2 number',
    4: 'View problems in specific subject and difficulty',
    5: 'View min , max and avg of submits for problems in specific subject and difficulty',
    6: 'View solve ratio problems by subject',
    7: 'View solve ratio problems by subject(all subjects) for specific company',
    8: 'View subjects of specific company',
    9: 'Change difficulty of specific problem',
    10: 'Change difficulty of specific problem for specific company with subject(s)',
    11: 'Delete problems of specific company',
    12: 'View min and max of difficulty of specific subject',
    13: 'Sort subjects on average of difficulty',
    14: 'Sort companies on average of difficulty',
    15: 'Sort subjects on solve ratio',
    16: 'View problems by subject for specific company(s)',
    17: 'Exit',
}


def print_menu():
    for key in menu_options.keys():
        print(key, '--', menu_options[key])


def print_table_of_problems(answer):
    index = 0
    for row in answer:
        print(f"subject='{row.tag}', difficulty={row.difficulty}, id='{row.id}', company='{row.company}', "
              f"solved={row.solved}, submits={row.submits}, time step={row.time_step}, title='{row.title}'"
              f", type='{row.type}'")
        index += 1
        if index > 50:
            if input('do u want to see more?(y/n) :') == 'y':
                index = 0
            else:
                break


def view_problems_by_tag_option():
    answer = ''
    subject = input('Enter your subject: ')
    sort_choice = int(input('Enter sort by (0-no sort, 1-by difficulty, 2-submits, 3-solved): '))

    if sort_choice == 0:
        answer = view_problems_by_tag(subject)
    elif sort_choice == 1:
        answer = view_problems_by_tag_sort_on_diff(subject)
    elif sort_choice == 2:
        answer = view_problems_by_tag_sort_on_submits(subject)
    elif sort_choice == 3:
        answer = view_problems_by_tag_sort_on_solved(subject)
    else:
        print('Invalid option. Please enter a number between 0 and 3.')
        view_problems_by_tag_option()

    print_table_of_problems(answer)


def view_submits_between_option():
    answer = ''
    start = int(input("Enter start: "))
    end = int(input("Enter end: "))

    sort_choice = int(input('Enter sort by (0-no sort, 1-by difficulty, 2-submits, 3-solved): '))

    if sort_choice == 0:
        answer = view_difficulty_between(start, end)
    elif sort_choice == 1:
        answer = view_difficulty_between_sort_on_diff(start, end)
    elif sort_choice == 2:
        answer = view_difficulty_between_sort_on_submits(start, end)
    elif sort_choice == 3:
        answer = view_difficulty_between_sort_on_solved(start, end)
    else:
        print('Invalid option. Please enter a number between 0 and 3.')
        view_submits_between_option()

    print_table_of_problems(answer)


def view_difficulty_between_option():
    answer = ''
    start = int(input("Enter start: "))
    end = int(input("Enter end: "))

    sort_choice = int(input('Enter sort by (0-no sort, 1-by difficulty, 2-submits, 3-solved): '))

    if sort_choice == 0:
        answer = view_submits_between(start, end)
    elif sort_choice == 1:
        answer = view_submits_between_sort_on_diff(start, end)
    elif sort_choice == 2:
        answer = view_submits_between_sort_on_submits(start, end)
    elif sort_choice == 3:
        answer = view_submits_between_sort_on_solved(start, end)
    else:
        print('Invalid option. Please enter a number between 0 and 3.')
        view_difficulty_between_option()

    print_table_of_problems(answer)


def view_diff_tag_option():
    subject = input('Enter your subject: ')
    diff_number = int(input("Enter the difficulty: "))
    answer = ''

    sort_choice = int(input('Enter sort by (0-no sort, 1-submits, 2-solved): '))

    if sort_choice == 0:
        answer = view_diff_tag(subject, diff_number)
    elif sort_choice == 1:
        answer = view_diff_tag_sort_on_submits(subject, diff_number)
    elif sort_choice == 2:
        answer = view_diff_tag_sort_on_solved(subject, diff_number)
    else:
        print('Invalid option. Please enter a number between 0 and 2.')
        view_diff_tag_option()

    print_table_of_problems(answer)


def view_diff_tag_min_max_avg_option():
    subject = input('Enter your subject: ')
    diff_number = int(input("Enter the difficulty: "))

    answer = view_diff_tag_min_max_avg(subject, diff_number)

    print(f"min submits={answer.one().system_min_submits}, max submits={answer.one().system_max_submits}"
          f", avg submits={answer.one().system_avg_submits}")


def view_solve_ratio_problems_by_tag_option():
    subject = input('Enter your subject: ')
    answer = view_solve_ratio_problems_by_tag(subject)
    index = 0
    for row in answer:
        print(f"ratio='{row.cast_solved_as_decimal____submits}', subject={row.tag}")
        index += 1
        if index > 50:
            if input('do u want to see more?(y/n) :') == 'y':
                index = 0
            else:
                break


def view_solve_ratio_problems_by_tag_company_option():
    company = input('Enter your company: ')
    subject = input('Enter your subject(Enter \'all\' for select all subjects): ')
    answer = ''

    if subject == 'all':
        answer = view_solve_ratio_problems_by_tag_company_all_tags(company)
    else:
        answer = view_solve_ratio_problems_by_tag_company(subject, company)

    index = 0
    for row in answer:
        print(f"id='{row.id}', ratio='{row.cast_solved_as_decimal____submits}', subject={row.tag}")
        index += 1
        if index > 50:
            if input('do u want to see more?(y/n) :') == 'y':
                index = 0
            else:
                break


def view_tags_of_company_option():
    company = input('Enter your company: ')

    answer = view_tags_of_company(company)
    index = 0
    for row in answer:
        print(f"subject='{row.tag}', company={row.company}")
        index += 1
        if index > 50:
            if input('do u want to see more?(y/n) :') == 'y':
                index = 0
            else:
                break


def change_difficulty_option():
    problem_id = input('Enter your problem id: ')
    new_diff_number = int(input("Enter the difficulty you want to set: "))
    change_difficulty(problem_id, new_diff_number)


def change_diff_company_tag_option():
    company = input('Enter your company: ')
    subjects = [input('Enter your subject(s): ')]
    print('enter more subjects or enter 0: ')
    while True:
        subject = input()
        if subject == "0":
            break
        subjects.append(subject)
    new_diff_number = int(input("Enter the difficulty you want to set: "))
    change_diff_company_tag(company, subjects, new_diff_number)


def delete_company_problems_option():
    company = input('Enter your company: ')
    delete_company_problems(company)


def view_min_max_diff_on_tags_option():
    subject = input('Enter your subject: ')
    answer = view_min_max_diff_on_tags(subject)
    print(f"min difficulty={answer.one().system_min_difficulty}, max difficulty={answer.one().system_max_difficulty}")


def sort_tags_on_average_option():
    answer = sort_tags_on_average()

    index = 0
    for row in answer:
        print(f"subject={row.tag}, avg of difficulty={row.avg_diff}")
        index += 1
        if index > 50:
            if input('do u want to see more?(y/n) :') == 'y':
                index = 0
            else:
                break


def sort_companies_on_average_option():
    answer = sort_companies_on_average()

    index = 0
    for row in answer:
        print(f"company={row.company}, avg of difficulty={row.avg_diff}")
        index += 1
        if index > 50:
            if input('do u want to see more?(y/n) :') == 'y':
                index = 0
            else:
                break


def sort_tags_on_solve_ratio_option():
    answer = sort_tags_on_solve_ratio()

    index = 0
    for row in answer:
        print(f"subject={row.tag}, solve ratio={row.solve_ratio}")
        index += 1
        if index > 50:
            if input('do u want to see more?(y/n) :') == 'y':
                index = 0
            else:
                break


def view_problems_by_tag_of_company_option():  # todo
    companies = [input('Enter your company(s): ')]
    print('enter more companies or enter 0: ')
    while True:
        company = input()
        if company == "0":
            break
        companies.append(company)
    subject = input('Enter your subject: ')

    answer = view_problems_by_tag_of_company(subject, companies)
    print_table_of_problems(answer)


if __name__ == '__main__':
    while True:
        print_menu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except:
            print('Wrong input. Please enter a number ...')

        if option == 1:
            view_problems_by_tag_option()
        elif option == 2:
            view_submits_between_option()
        elif option == 3:
            view_difficulty_between_option()
        elif option == 4:
            view_diff_tag_option()
        elif option == 5:
            view_diff_tag_min_max_avg_option()
        elif option == 6:
            view_solve_ratio_problems_by_tag_option()
        elif option == 7:
            view_solve_ratio_problems_by_tag_company_option()
        elif option == 8:
            view_tags_of_company_option()
        elif option == 9:
            change_difficulty_option()
        elif option == 10:
            change_diff_company_tag_option()
        elif option == 11:
            delete_company_problems_option()
        elif option == 12:
            view_min_max_diff_on_tags_option()
        elif option == 13:
            sort_tags_on_average_option()
        elif option == 14:
            sort_companies_on_average_option()
        elif option == 15:
            sort_tags_on_solve_ratio_option()
        elif option == 16:
            view_problems_by_tag_of_company_option()
        elif option == 17:
            print('Thanks message before exiting')
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 4.')
