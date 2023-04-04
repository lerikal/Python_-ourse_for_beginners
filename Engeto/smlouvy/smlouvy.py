def main():
    contract = input_type_of_doc()
    while contract not in range(2):
        input_type_of_doc()

    employees = ['X12345', 'X54321']

    for employer in employees:
        info_employer = empl_data(employer)
        final_document = generate_doc(contract, info_employer)
        print(save_document(final_document, employer))
    print('Contracts have been generated.')

def input_type_of_doc():
    return int(input('Please select the option number of action you want to perform:\n0. salary change \n1. job change '
                     '\n2. contract prolongation\n '))

def create_template(document):
    template = document.read()
    document.close()
    return template

def select_document(contract):
    if contract == 0:
        document = open('C:\\Users\\uzivatel\\PycharmProjects\\pythonProject\\smlouvy\\salary_change.txt', 'rt')
        return create_template(document)
    elif contract == 1:
        document = open('C:\\Users\\uzivatel\\PycharmProjects\\pythonProject\\smlouvy\\job_change.txt')
        return create_template(document)
    elif contract == 2:
        document = open('C:\\Users\\uzivatel\\PycharmProjects\\pythonProject\\smlouvy\\contract_prolongation.txt')
        return create_template(document)

def empl_data(employer):
    data = open('C:\\Users\\uzivatel\\PycharmProjects\\pythonProject\\smlouvy\\employees.txt', 'rt')
    empl = data.read()
    data.close()
    data_employer = eval(empl)
    info_employer = data_employer.get(employer)
    return info_employer

def generate_doc(contract, info_employer):
    if contract == 0:
        final_document = select_document(contract).format(full_name=info_employer.get('full_name'),
                                                          ID=info_employer.get('ID'),
                                                          birthdate=info_employer.get('birthdate'),
                                                          salary=info_employer.get('salary'))
    elif contract == 1:
        final_document = select_document(contract).format(full_name=info_employer.get('full_name'),
                                                          ID=info_employer.get('ID'),
                                                          birthdate=info_employer.get('birthdate'),
                                                          job_title=info_employer.get('job_title'),
                                                          position_from=info_employer.get('position_from'))
    elif contract == 2:
        final_document = select_document(contract).format(full_name=info_employer.get('full_name'),
                                                          ID=info_employer.get('ID'),
                                                          birthdate=info_employer.get('birthdate'),
                                                          contract_end=info_employer.get('contract_end'))
    return final_document

def save_document(final_document, employer):
    final = open(r'C:\\Users\\uzivatel\\PycharmProjects\\pythonProject\\smlouvy\\finalni_dokument_{}.txt'.format(employer), 'w')
    final.write(final_document)
    final.close()
    return 'Creating contract for {} ....'.format(employer)

main()
