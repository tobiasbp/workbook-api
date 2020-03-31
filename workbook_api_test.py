import configparser
import random

from workbook_api import WorkbookAPI

# Object for parsing config file
config = configparser.ConfigParser()

# Read the config file
config.read("workbook_api_test.conf")

# Create an instance of the Workbook API
api = WorkbookAPI(
  config.get('workbook', 'url'),
  config.get('workbook', 'login'),
  config.get('workbook', 'password'),
  )

PROJECT_KEYS = set({
  'Active',
  'ColorId',
  'Id',
  'ProjectFolder',
  'ProjectName',
  'ProjectNumber',
  'ProjectRetainer',
  'ProjectRetainerAllowDeliveryJobToExceedMasterBudgetWhenClosed',
  'ProjectRetainerIsMixedRetainer',
  'ProjectRetainerSummarizeActivityLines',
  'ResourceId'
  #'ResponsibleResourceId',
  #'UpdateDate',
  #'UpdateResourceId'
  })

CAPACITY_PROFILE_KEYS = set({
  "Id",
  "ResourceId",
  "HoursNormalMonday",
  "HoursNormalTuesday",
  "HoursNormalWednesday",
  "HoursNormalThursday",
  "HoursNormalFriday",
  "HoursNormalSaturday",
  "HoursNormalSunday",
  "HoursFlexMonday",
  "HoursFlexTuesday",
  "HoursFlexWednesday",
  "HoursFlexThursday",
  "HoursFlexFriday",
  "HoursFlexSaturday",
  "HoursFlexSunday",
  "HoursIdealMonday",
  "HoursIdealTuesday",
  "HoursIdealWednesday",
  "HoursIdealThursday",
  "HoursIdealFriday",
  "HoursIdealSaturday",
  "HoursIdealSunday",
  "ValidFrom"
  #"OfficeHoursMondayStart",
  #"OfficeHoursMondayEnd",
  #"OfficeHoursTuesdayStart",
  #"OfficeHoursTuesdayEnd",
  #"OfficeHoursWednesdayStart",
  #"OfficeHoursWednesdayEnd"
  #"OfficeHoursThursdayStart",
  #"OfficeHoursThursdayEnd",
  #"OfficeHoursFridayStart",
  #"OfficeHoursFridayEnd",
  #"OfficeHoursSaturdayStart",
  #"OfficeHoursSaturdayEnd",
  #"OfficeHoursSundayStart",
  #"OfficeHoursSundayEnd"
  })

COMPANY_KEYS =set({
  'Active',
  'Id',
  'Name'
  })

COSTUMER_KEYS = set({
  'Active',
  'ActivityGrouping',
  'AllowInvoiceExceedApprovedPriceQuote',
  'AllowInvoiceWithoutApprovedPriceQuote',
  'AllowMultiResource',
  'AllowPriceQuoteExceedClientOrder',
  'CompDepartmentId',
  'CopyPrintSettingsNewPrice',
  'CurrencyId',
  #'CustCode1',
  #'CustCode2',
  #'CustCode3',
  #'CustCode4',
  #'CustCode5',
  'CustomerAccountNumberRequiredOnInvoice',
  'CustomerInvoiceApprovalHandlingActivated',
  'CustomerOrderNumberRequiredOnInvoice',
  'DeliveryAddress',
  'EnableInterCompanySettlement',
  'Id',
  'InterCompanyTimeRegistrationAllowed',
  'InterCompanyVouchRegistrationAllowed',
  'InvoiceAllowEditExternalExpenseFactor',
  'InvoiceAllowEditTimeSale',
  'InvoiceCustomerOrderNumberRequired',
  'JobCreateAddDebtor',
  'JobEstimateRequired',
  'LanguageId',
  'MaterialCalculationAllowChangeSaleHours',
  'MaterialGroupId',
  'MoveActivityLine',
  'Name',
  'PaymentTermId',
  'PlanForegroundColorNumber',
  'PriceQuoteAddress',
  'PriceQuoteAllowChangeExternalExpenseFactor',
  'PriceQuoteAllowChangeTimeSale',
  'PriceQuoteBlockIfDeviation',
  'PriceQuoteVatShow',
  'PriceQuoteVatValue',
  'ProjectId',
  'ResponsibleEmployeeId',
  'ShowActivity',
  'ShowActivityHours',
  'ShowActivityLine',
  'ShowActivityPrice',
  'ShowPaymentPlan',
  'ShowPhase',
  'ShowPhasePrice',
  'TypeId',
  'UseFixedDebtorAddressOnPriceQuoteCreation'
  })

DEPARTMENT_KEYS = set({
  'CompanyId',
  'Id',
  'Name',
  #'ResponsibleId'
  })

DEBTOR_BALANCE_KEYS = set({
  "Id",
  "ArpAccountNumber",
  "ArpAccountName",
  "ArpGroupTitle",
  #"AccountContact",
  #"AccountContactTel",
  #"RemainingAmountTotal",
  #"RemainingAmountDue",
  "CompanyId",
  "ArpAccountType",
  "Blocked",
  "ArpAccountGrpId",
  #"Email",
  "CurrencyId",
  "Employee",
  "RequestStatus",
  #"RequestRejectComment",
  "HasOpenEliminationItems"
  })

DEBTOR_KEYS = set({
  'AccountNumber',
  'AccountType',
  #'Address1',
  #'Address2',
  'AllowCombinedPayment',
  'Blocked',
  #'City',
  'CompanyId',
  #'ContactName',
  'CountryId',
  'CreateEmployeeId',
  'CreditorAllowedZeroPricefactor',
  'CreditorSendRemittanceAdvice',
  'CurrencyID',
  'DebtorPaymentMethodId',
  'DebtorPaymentTermId',
  'DebtorVATId',
  'DeliveryDebtorOnly',
  #'EAN',
  #'Email',
  'EmployeeCreditor',
  'ExpenseEntryVoucherCurrencyMethod',
  'Id',
  'Internal',
  'LanguageId',
  'Name',
  'PayPropDisabled',
  'PayPropOmitCreditNote',
  'PayPropSkipAllIfCreditNote',
  'PayPropSkipAllIfDebitAmount',
  #'PhoneNumber',
  'PostingGroupId',
  'PrintStatement',
  #'PublicRegNoCheck',
  'PublicRegNoCheckType',
  #'PublicRegistrationNumber',
  #'ReportingGroupId',
  'RequestStatus',
  #'UpdateResourceId',
  'UseReminderHandling',
  #'ZipCode'
  })

JOB_KEYS = set({
  'AdjustmentHandlingExtExp',
  'AdjustmentHandlingExtExpCost',
  'AdjustmentHandlingExtraDiscount',
  'AdjustmentHandlingMat',
  'AdjustmentHandlingTime',
  'AdminOnly',
  'Billable',
  'BillingExternalExpenseType',
  'BillingMileageType',
  'BillingTimeEntryTravelTimeType',
  'CapitalizeSalesInvoice',
  'CompDepId',
  'CompanyCurrencyId',
  'CompanyDepartmentId',
  'CompanyId',
  'CompletePhase',
  'CreateDate',
  'CreateEmpId',
  'CreateEmployeeId',
  #'CustGrpId',
  'CustomerId',
  'CustomerName',
  'DoMakeWipAdjustment',
  'EmployeeAccessType',
  'EndDate',
  'ExpAccMtd',
  'ExpenseEntryAllowed',
  'ExternalUserAccessType',
  'FlexTimeRegDisabled',
  'FolderArchived',
  'FolderExtra',
  'Id',
  'IsMediaJob',
  'JobAccessType',
  'JobFolderArkiveret',
  'JobFolderXtra',
  'JobID',
  'JobName',
  'JobResponsibleId',
  'JobRessAnsvarID',
  'JobStart',
  'JobStatusId',
  'JobTaskActive',
  'JobTaskUseAllDays',
  'JobTypeId',
  'JournalNumber',
  'LeveringsDato',
  'MaterialRegAllowed',
  'MileageEntryAllowed',
  #'PostDate',
  'PostMethodExt',
  'PostMethodMat',
  'PostMethodTime',
  'PostSpecId',
  'PricelistID',
  'ProjectId',
  'ProjectRetainerDeliveryJob',
  'ProjectRetainerMasterJob',
  'Public',
  'PurchaseOrderAllowed',
  'ResponsibleId',
  'RetainerJob',
  'StartDate',
  'StatusId',
  'SubsistenceAllowanceAllowed',
  'SuppTxtRequested',
  'SupplementaryTextRequested',
  'SupportTicketEnable',
  'TeamID',
  'TeamId',
  'TemplateJob',
  'TimeAndMaterial',
  'TimeEntryAllowed',
  'TimeRegAllow',
  'VoucherRegistrationAllowed'
  })

JOB_TYPE_KEYS = set({
  'Active',
  'Id',
  'Name',
  'RetainerJob',
  #'UpdateDate',
  'UpdatePriceQuote',
  #'UpdateResourceId'
  })

EMPLOYEE_KEYS = set({
  'Active',
  'AllowCreateSkills',
  'AllowCreateTags',
  'AllowCreditorEdit',
  'AllowDebtorEdit',
  'AllowExpenseEntry',
  'AllowFinanceAccountEdit',
  'AllowSaveNewJobTemplates',
  'AllowVATEdit',
  'AllowVendorInvoiceQuickRegistration',
  'CloseDownSystem',
  'CompanyId',
  'DefaultActivityId',
  'DepartmentId',
  'DisplayCurrencyId',
  'DocumentFormatStandard',
  'DriveRegistrationNumberRefund',
  'EmailBodyFormatType',
  'EmployeeName',
  'EmployeePosition',
  'EmploymentTypeId',
  'ExternalCalenderSync',
  #'ExternalCode',
  'FlexDisabled',
  #'FollowUpRefresh',
  #'FullClientAccess',
  'HireDate',
  'Id',
  'ManagerResourceId',
  'NewbizzResourceAccess',
  'PermanentlyDisabled',
  'ReimbursementApproveManagerResourceId',
  #'Sex',
  #'SubstituteEmployeeId',
  'SystemLogOn',
  'SystemSetting',
  'TimeRegistration',
  'TimeRegistrationReceiveMail',
  'TimeSheetApproverResourceId'
  })

EMPLOYEE_POSITION_KEYS = set({
  "Id",
  "Title",
  #"Description",
  #"CapacityPlanEmployeeId",
  "UpdateResourceId",
  "Update",
  "UpdateType"
  })

RESOURCE_KEYS = set({
  'Active',
  'AllowBulkEmail',
  'AllowEmail',
  'AllowMail',
  'AllowPhone',
  'AllowSendMarketing',
  'AllowSms',
  #'ApplicationAccessRoleId',
  'CalendarShowExternalInTaskList',
  #'CreateByResourceId',
  #'CreateDate',
  #'Email',
  'Id',
  'Initials',
  #'InterfaceLCID',
  'IsLeadSource',
  'IsPartner',
  'LDAPLogin',
  'Name',
  #'ParentResourceId',
  #'ReleaseState',
  #'ReportLCID',
  'ResourceBookable',
  #'ResourceFolder',
  'TimeEntryShowOnLogin',
  'TypeId',
  'UpdateDate',
  'UpdatedByResourceId',
  'UsedAsSupplier',
  'UserAccess',
  #'UserLogin'
  })

EXPENSE_ENTRY_KEYS = set([
  'ApprovalStatus',
  'CompanyId',
  'CreditorId',
  #'CurrencyAmount',
  'CurrencyId',
  #'Description',
  'ExpenseEntryTypeId',
  'Id',
  'IsApproved',
  #'LocationId',
  #'ReceiptFile',
  'ResourceId',
  #'TaxManualEdited',
  'UpdateDate',
  'UpdateResId',
  #'VoucherCompanyId',
  #'VoucherDate',
  #'VoucherNumber'
  ])

EMPLOYEE_PRICE_GROUPS_KEYS = set({
  'Active',
  'Id',
  'PriceGroupName'
  })

EMPLOYEE_PRICES_HOUR_KEYS = set({
  'CurrencyId',
  'EmployeeId',
  #'HoursCost',
  #'HoursSale',
  'Id',
  'Profit',
  'ValidFrom'
  })

INVOICE_KEYS = set({
  #'AmountNet',
  #'AmountNetCurrency',
  #'AmountTot',
  #'AmountTotalCurrency',
  #'AmountVat',
  #'AmountVatCurrency',
  #'Comment',
  'CreditNoteCloseJob',
  'CurrencyDate',
  'CurrencyId',
  'CurrencyRate',
  'Date',
  'DebtorId',
  'DebtorLabel',
  'DoIndentLines',
  'DoNotCapitalize',
  #'DueDate',
  'EliminatePartInvoice',
  'Headline',
  'Id',
  'IncludeVouchers',
  'Internal',
  #'InternalComment',
  'JobId',
  'JournalNumber',
  'LanguageId',
  'MainInvoice',
  #'Number',
  #'NumberNumeric',
  'PartialInvoiceExpPostIsApproved',
  'PayModeId',
  'PayTermId',
  'PayTermText',
  'PaymentStatusForSystemsWithoutFinance',
  #'PostDate',
  #'PrintDate',
  #'PrintResourceId',
  'ReportLayoutId',
  #'ReportWatermarkId',
  'ResponsibleResourceId',
  'ReverseCharge',
  'ShowCurrency',
  'ShowDecimals',
  'ShowDividingLines',
  'ShowLineHours',
  'ShowLineHoursPrice',
  'ShowLinePrice',
  'ShowLines',
  'ShowPartInvoiceExpenseDetails',
  'ShowPhaseNumber',
  'ShowPhasePrice',
  'ShowPhases',
  'ShowVATPercent',
  'Status',
  'SubInvoice',
  'Title',
  'TypeId',
  'UseActGrouping',
  #'VATPercent'
  })

INVOICE_TYPE_KEYS = set({
  'Description',
  'Id'
  })

CREDITOR_KEYS = set({
  'AccountId',
  'AccountNumber',
  'AccountType',
  #'Address1',
  'AllowCombinedPayment',
  'Blocked',
  #'City',
  'CompanyId',
  #'CountryId',
  #'CountryStateId',
  #'CreditorActivityId',
  'CreditorAllowedZeroPricefactor',
  'CreditorIsEmployee',
  'CreditorOffAccountAuto',
  #'CurrencyId',
  'DeliveryDebtorOnly',
  'ExpenseEntryVoucherCurrencyMethod',
  'Id',
  'Internal',
  'IsMiscAccount',
  'Name',
  #'PayGroupId',
  'PayMethodId',
  'PayModeId',
  'PayPropDisabled',
  'PayPropOmitCreditNote',
  'PayPropSkipAllIfCreditNote',
  'PayPropSkipAllIfDebitAmount',
  'PrintStatement',
  'PublicRegistrationNumberCheckType',
  #'RemainingAmountDue',
  #'RemainingAmountTotal',
  #'SupplierResourceID',
  #'UpdateResourceId',
  'UseReminderHandling'
  })

CURRENCY_KEYS = set({
  'Blocked',
  'Id',
  'Iso4127',
  'IsoCode',
  'Name',
  'ReportingCurrency'
  })

CREDITOR_KEYS_OLD = set({
  'AccountNumber',
  'AccountType',
  #'Address1',
  #'AllowCombinedPayment',
  #'BankAccountNumber',
  #'BankRegistrationNumber',
  'Blocked',
  #'City',
  'CompanyId',
  #'CountryId',
  #'CreateEmployeeId',
  #'CreditorActivityId',
  #'CreditorAllowedZeroPricefactor',
  #'CreditorPaymentDefinitionId',
  #'CreditorPaymentMethodId',
  #'CreditorPaymentTermId',
  #'CreditorSendRemittanceAdvice',
  #'CreditorVATId',
  #'CurrencyID',
  'DeliveryDebtorOnly',
  #'EmployeeCreditor',
  #'ExpenseEntryVoucherCurrencyMethod',
  'Id',
  #'Internal',
  #'LanguageId',
  'Name',
  #'PayPropDisabled',
  #'PayPropOmitCreditNote',
  #'PayPropSkipAllIfCreditNote',
  #'PayPropSkipAllIfDebitAmount',
  #'PostingGroupId',
  #'PrimarySupplyType',
  #'PrintStatement',
  #'PublicRegNoCheck',
  #'PublicRegNoCheckType',
  #'PublicRegistrationNumber',
  #'ReportingGroupId',
  'RequestStatus',
  #'SupplierResourceID',
  #'UpdateResourceId',
  #'UseReminderHandling',
  #'ZipCode'
  })

TIME_ENTRY_KEYS = set({
    'ActivityId',
    'ApprovalStatus',
    'Billable',
    'Correction',
    'Cost',
    'CostCurrencyAmount',
    'CostCurrencyId',
    #'CostMethod',
    'CreateDate',
    'CreateResourceId',
    'DeletedMarked',
    'DescriptionRequired',
    'HoursMoved',
    'Id',
    'JobId',
    'JournalNumber',
    'PostDate',
    'PricelistId',
    'Public',
    'RegistrationDate',
    'ResourceId',
    'Sale',
    'SaleCurrencyAmount',
    'SaleCurrencyId',
    'SequenceNumber',
    #'TariffAdditionalPercentCost',
    #'TariffAdditionalPercentIcSale',
    #'TariffAdditionalPercentSale',
    'UpdateDate',
    'UpdateResourceId',
    'UpdateType'
    })

FINANCE_ACCOUNT_KEYS = set({
    'AccountDescription',
    'AccountNumber',
    'AccountType',
    'AllowVendorInvoice',
    'Automatic',
    'Blocked',
    'CompanyId',
    'DimensionNotAllowed',
    'DimensionRequired',
    'Id',
    'LineNumber',
    'ReportPageBreak'
    })

#FIXME: Test limited searches

def test_get_finance_account():
  accounts = api.get_finance_accounts()
  assert isinstance(accounts, list), "Finance accounts entries is a list"
  for a in accounts:
    assert FINANCE_ACCOUNT_KEYS.issubset(a.keys()), "Finance account entry has all keys"
  #account = random.choice(accounts)
  account = api.get_finance_account(
    account_id=random.choice(accounts)['Id'])
  assert FINANCE_ACCOUNT_KEYS.issubset(account.keys()), "Finance account has all keys"
  

def test_get_capacity_profiles():
    # Get a random employee
    employee = random.choice(api.get_employees())
    assert isinstance(employee, dict), "Employee is a dict"
    # Get capacity profiles for random employee
    profiles = api.get_capacity_profiles(employee['Id'])
    assert isinstance(profiles, list), "Capacity profiles is a list"
    assert len(profiles) > 0, "All employees have at least 1 capacity profile"
    for p in profiles:
        print(CAPACITY_PROFILE_KEYS - p.keys())
        assert CAPACITY_PROFILE_KEYS.issubset(p.keys()), "Capacity profiles has all keys"


def test_get_time_entries():
    # Random active job
    j = random.choice(api.get_jobs(Status=[1]))
    # Get entries for random job
    entries = api.get_time_entries(JobId=j['Id'])
    assert isinstance(entries, list), "Time entries is a list"
    for e in entries:
        print(TIME_ENTRY_KEYS - e.keys())
        assert TIME_ENTRY_KEYS.issubset(e.keys()), "Time entry has all keys"

def test_currency_convert():
    currencies = api.get_currencies()
    companies = api.get_companies()
    cur1_id = currencies[0]['Id']
    cur2_id = currencies[-1]['Id']
    comp_id = random.choice(companies)['Id']
    amount = random.random()
    r = api.currency_convert(
        Amount=amount,
        FromCurrencyId=cur1_id,
        ToCurrencyId=cur2_id,
        CompanyId=comp_id
        )
    assert isinstance(r, float), "Converted amount is a float"
    # Convert to same currency
    r = api.currency_convert(
        Amount=amount,
        FromCurrencyId=cur1_id,
        ToCurrencyId=cur1_id,
        CompanyId=comp_id
        )
    assert r == amount, "Convert to same currency is same amount"


def test_get_employee_price_groups():
  employee_price_groups = api.get_employee_price_groups()
  assert isinstance(employee_price_groups, list), "Employee price groups entries is a list"
  for e in employee_price_groups:
    assert EMPLOYEE_PRICE_GROUPS_KEYS.issubset(e.keys()), "Employee price groups entry has all keys"

def test_get_employee_positions():
  employee_positions = api.get_employee_positions()
  assert isinstance(employee_positions, list), "Employee positions is a list"
  for p in employee_positions:
    #print(EMPLOYEE_POSITION_KEYS - p.keys())
    assert EMPLOYEE_POSITION_KEYS.issubset(p.keys()), "Employee positions entry has all keys"


def test_get_expense_entries():
  expense_entries = api.get_expense_entries()
  assert isinstance(expense_entries, list), "Expense entries is a list"
  for e in expense_entries:
    #print(EXPENSE_ENTRY_KEYS - e.keys())
    assert EXPENSE_ENTRY_KEYS.issubset(e.keys()), "Expense entry has all keys"


def test_get_companies():
  companies = api.get_companies()
  assert isinstance(companies, list), "Companies is a list"
  for c in companies:
    assert COMPANY_KEYS.issubset(c.keys()), "Company has all keys"


def test_get_costumers():
  costumers = api.get_costumers()
  assert isinstance(costumers, list), "Costumers is a list"
  for c in costumers:
    assert COSTUMER_KEYS.issubset(c.keys()), "Costumer has all keys"


def test_get_creditors():
  creditors = api.get_creditors()
  assert isinstance(creditors, list), "Creditors is a list"
  for c in creditors:
    assert CREDITOR_KEYS.issubset(c.keys()), "Creditor has all keys"


def test_get_currencies():
  currencies = api.get_currencies()
  assert isinstance(currencies, list), "Currencies is a list"
  for c in currencies:
    assert CURRENCY_KEYS.issubset(c.keys()), "Currency has all keys"


def test_get_departments():
  departments = api.get_departments()
  assert isinstance(departments, list), "Departments is a list"
  for d in departments:
    print(DEPARTMENT_KEYS - d.keys())
    assert DEPARTMENT_KEYS.issubset(d.keys()), "Department has all keys"


def test_get_debtors():
  debtors = api.get_debtors()
  assert isinstance(debtors, list), "Debtors is a list"
  for d in debtors:
    print(DEBTOR_KEYS - d.keys())
    assert DEBTOR_KEYS.issubset(d.keys()), "Debtor has all keys"


def test_get_debtors_balance():
  debtors = api.get_debtors_balance(company_id=1)
  assert isinstance(debtors, list), "Debtors balance is a list"
  for d in debtors:
    assert DEBTOR_BALANCE_KEYS.issubset(d.keys()), "Debtor balance has all keys"


def test_get_invoices():
  invoices = api.get_invoices()
  assert isinstance(invoices, list), "Invoices is a list"
  for i in invoices:
    print(INVOICE_KEYS - i.keys())
    assert INVOICE_KEYS.issubset(i.keys()), "Invoice has all keys"


def test_get_invoice_type():
  invoice_types = api.get_invoice_types()
  assert isinstance(invoice_types, list), "Invoice types is a list"
  for i in invoice_types:
    assert INVOICE_TYPE_KEYS.issubset(i.keys()), "Invoice type has all keys"


def test_get_jobs():
  jobs = api.get_jobs()
  assert isinstance(jobs, list), "Jobs is a list"
  for j in jobs:
    assert JOB_KEYS.issubset(j.keys()), "job has all keys"


def test_get_job():
  # Get random job
  j1 = random.choice(api.get_jobs())
  assert isinstance(j1, dict), "Random job is a dict"
  assert JOB_KEYS.issubset(j1.keys()), "Random job has all keys"
  # Use Id of random job to look up a single job
  j2 = api.get_job(Id=j1['Id'])
  assert isinstance(j2, dict), "Job is a dict"
  assert JOB_KEYS.issubset(j2.keys()), "Single job has all keys"
  assert j1 == j2, "Jobs are identical"

def test_get_job_types():
  job_types = api.get_job_types()
  assert isinstance(job_types, list), "Job types is a list"
  for jt in job_types:
    print(JOB_TYPE_KEYS - jt.keys())
    assert JOB_TYPE_KEYS.issubset(jt.keys()), "Job type has all keys"

def test_get_employees():
  employees = api.get_employees()
  assert isinstance(employees, list), "Employees is a list"
  for e in employees:
    #print(EMPLOYEE_KEYS - e.keys())
    assert EMPLOYEE_KEYS.issubset(e.keys()), "Employee has all keys"


def test_get_employee():
  # Get a random employee
  e1 = random.choice(api.get_employees())
  assert isinstance(e1, dict), "Random employee is a dict"
  assert EMPLOYEE_KEYS.issubset(e1.keys()), "Random employee has all keys"
  # Use Id of random employee to look up a single employee
  e2 = api.get_employee(Id=e1['Id'])
  assert isinstance(e2, dict), "Employee is a dict"
  assert EMPLOYEE_KEYS.issubset(e2.keys()), "Single employee has all keys"
  assert e1 == e2, "Employees are identical"


def test_get_projects():
  projects = api.get_projects()
  assert isinstance(projects, list), "projects is a list"
  for p in projects:
    assert PROJECT_KEYS.issubset(p.keys()), "Project has all keys"


def test_get_resources():
  resources = api.get_resources()
  assert isinstance(resources, list), "Resources is a list"
  for r in resources:
    assert RESOURCE_KEYS.issubset(r.keys()), "Resource has all keys"


def test_get_employee_prices_hour():
  prices = api.get_employee_prices_hour()
  assert isinstance(prices, list), "Prices is a list"
  for p in prices:
    print(EMPLOYEE_PRICES_HOUR_KEYS - p.keys())
    assert EMPLOYEE_PRICES_HOUR_KEYS.issubset(p.keys()), "Prices has all keys"
  # Test filter
  random_price = random.choice(prices)
  prices = api.get_employee_prices_hour(PriceGroupId=random_price['EmployeeId'])
  for p in prices:
    print(EMPLOYEE_PRICES_HOUR_KEYS - p.keys())
    assert EMPLOYEE_PRICES_HOUR_KEYS.issubset(p.keys()), "Prices has all keys"
    assert p['EmployeeId'] == random_price['EmployeeId']
  

def test_get_resource():
  # Get a random resource
  r1 = random.choice(api.get_resources())
  assert isinstance(r1, dict), "Random resource is a dict"
  assert RESOURCE_KEYS.issubset(r1.keys()), "Random resource has all keys"
  # Use Id of random resource to look up a single resource
  r2 = api.get_resource(Id=r1['Id'])
  assert isinstance(r2, dict), "Resource is a dict"
  assert RESOURCE_KEYS.issubset(r2.keys()), "Single resource has all keys"
  assert r1 == r2, "Resources are identical"

