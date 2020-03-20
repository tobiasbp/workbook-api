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
  'ResponsibleId'
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
  'PublicRegNoCheck',
  'PublicRegNoCheckType',
  #'PublicRegistrationNumber',
  #'ReportingGroupId',
  'RequestStatus',
  'UpdateResourceId',
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
  'UpdateDate',
  'UpdatePriceQuote',
  'UpdateResourceId'
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
  'SubstituteEmployeeId',
  'SystemLogOn',
  'SystemSetting',
  'TimeRegistration',
  'TimeRegistrationReceiveMail',
  'TimeSheetApproverResourceId'
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
  'LocationId',
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
  'HoursSale',
  'Id',
  'Profit',
  'ValidFrom'
  })


#FIXME: Test limited searches

def test_get_employee_price_groups():
  employee_price_groups = api.get_employee_price_groups()
  assert isinstance(employee_price_groups, list), "Employee price groups entries is a list"
  for e in employee_price_groups:
    assert EMPLOYEE_PRICE_GROUPS_KEYS.issubset(e.keys()), "Employee price groups entry has all keys"


def test_get_expense_entries():
  expense_entries = api.get_expense_entries()
  assert isinstance(expense_entries, list), "Expense entries is a list"
  for e in expense_entries:
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


def test_get_departments():
  departments = api.get_departments()
  assert isinstance(departments, list), "Departments is a list"
  for d in departments:
    assert DEPARTMENT_KEYS.issubset(d.keys()), "Department has all keys"


def test_get_debtors():
  debtors = api.get_debtors()
  assert isinstance(debtors, list), "Debtors is a list"
  for d in debtors:
    assert DEBTOR_KEYS.issubset(d.keys()), "Debtor has all keys"

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
    assert JOB_TYPE_KEYS.issubset(jt.keys()), "Job type has all keys"

def test_get_employees():
  employees = api.get_employees()
  assert isinstance(employees, list), "Employees is a list"
  for e in employees:
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
    #print(RESOURCE_KEYS - r.keys())
    assert RESOURCE_KEYS.issubset(r.keys()), "Resource has all keys"


def test_get_employee_prices_hour():
  prices = api.get_employee_prices_hour()
  assert isinstance(prices, list), "Prices is a list"
  for p in prices:
    print(EMPLOYEE_PRICES_HOUR_KEYS - p.keys())
    assert EMPLOYEE_PRICES_HOUR_KEYS.issubset(p.keys()), "Prices has all keys"


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

