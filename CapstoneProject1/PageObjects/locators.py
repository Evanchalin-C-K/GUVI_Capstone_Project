class Locators:
    username_locator = "username"  # Name
    password_locator = "password"  # Name
    login_button = "//button[@type='submit']"   # XPATH
    logout_dropdown = "//li[@class='oxd-userdropdown']//i"  # XPATH
    logout_button = "Logout"  # link_test

    pim_locator = "//ul[@class='oxd-main-menu']/li[2]"
    add_locator = '//button[text()=" Add "]'
    first_name = "//input[@name='firstName']"
    last_name = "//input[@name='lastName']"
    employee_id = "//div[@class='oxd-form-row']/div[2]//input"
    save_button = '// button[text() = " Save "]'

    # employee list
    employee_list = "//a[text()='Employee List']"
    employee_name = "//input[contains(@placeholder, 'Type')]"
    search_button = '//button[text()=" Search "]'
    edit_icon = "//i[@class='oxd-icon bi-pencil-fill']"
    license_num = "//form[@class='oxd-form']/div[2]/div[2]/div[1]//input"
    license_exp = "//form[@class='oxd-form']/div[2]/div[2]/div[2]//input"
    nationality = "//div[@class='oxd-select-wrapper']"
    indian = "//span[text()='Indian']"
    marital_status = "//form[@class='oxd-form']/div[3]/div/div[2]//div[@class='oxd-select-text--after']"
    # marital_status = "//div[@class='oxd-select-wrapper']"
    married = "//span[text()='Married']"
    dob_locator = "//form[@class='oxd-form']/div[3]/div[2]/div[1]//input"
    gender_female_btn = "//input[@value='2']"
    save_btn1 = "//form[@class='oxd-form']/div[5]/button"
    blood_group = "//div[@class='orangehrm-custom-fields']//i"
    blood_grp = "//span[text()='O+']"
    save_btn2 = "//form[@class='oxd-form']/div[2]/button"

    # job page
    job_locator = "//div[@role='tablist']/div[6]/a[text()='Job']"
    joined_date = "//div[@class='oxd-date-input']/input"
    job_title = "//div[@class='oxd-select-wrapper']"
    qa_engineer = "//span[text()='QA Engineer']"
    sub_unit = "//form[@class='oxd-form']/div/div/div[5]/div/div[2]//i"
    QA = "//span[text()='Quality Assurance']"
    save_btn_job = "//div[@class='oxd-form-actions']/button"

    # delete
    emp_name = "//label[text()='Employee Name']/../..//input"
    delete_icon = "//i[@class='oxd-icon bi-trash']"



