import configparser

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

def test_get_costumers():
  costumers = api.get_costumers()
  assert isinstance(costumers, list), "Costumers is a list"
  for c in costumers:
    assert COSTUMER_KEYS.issubset(c.keys()), "Costumer has all keys"


def test_get_jobs():
  jobs = api.get_jobs()
  assert isinstance(jobs, list), "Jobs is a list"
  for j in jobs:
    assert JOB_KEYS.issubset(j.keys()), "job has all keys"


def test_get_employees():
  employees = api.get_employees()
  assert isinstance(employees, list), "Employees is a list"


def test_get_projects():
  projects = api.get_projects()
  assert isinstance(projects, list), "projects is a list"
  for p in projects:
    assert PROJECT_KEYS.issubset(p.keys()), "Project has all keys"

