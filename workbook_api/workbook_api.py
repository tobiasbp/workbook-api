import requests

class UnexpectedStatusCode(Exception):
  """
  Raise this error when a call to the API
  returns a status code other than the one we expect
  """
  pass

class DataValidationError(Exception):
  """
  Raise this error if the API could not
  validate the data we gave it
  """

class WorkbookAPI():

  def __init__(self, url, user_name, password):

    # The authentication object to use
    self.auth = requests.auth.HTTPBasicAuth(user_name, password)

    # The session to use for all requests
    self.session = requests.Session()

    # Headers to send with every request
    #self.headers = {"Authorization": "Bearer " + access_token}

    # The base URL af all calls to the Float API
    #self.base_url = 'https://api.float.com/v3/{}'
    self.base_url = url


  def _get(self, path, params = {}):
    '''Args:
      path: The string added to the base URL
      params: key,value pairs to send in URL
    '''
    assert path[0] == '/', "Path must begin with slash"
    assert isinstance(path, str), "Path must be a string"

    # Build the URL
    url = self.base_url + path

    # Perform request
    r = self.session.get(url, params=params, auth=self.auth)

    # Raise exception on unexpected status code
    if r.status_code != 200:
      raise UnexpectedStatusCode("Got {} but expected 200".format(r.status_code))

    return r.json()


  def get_budgets(self, active=True):
    '''
    Get a list of budgets
    Implements: FinanceBudgetsRequest
    Params: active
    '''
    # FIXME: Untested
    path = '/finance/budgets'

    return self._get(path, params={})


  def get_capacity_profiles(self, ResourceId, AlwaysReturnProfile=True):
    '''Get a list of capacity profile for a resource (Human)
    Capcity is hours expected to work.
    Implements: CapacityProfilesByResourceRequest

    Keyword arguments:
    ResourceIds (List<Int>): List of resource IDs
    StartDate (String): The starting date to obtain capacities for
    EndDate (String): The ending date to obtain capacities for
    
    A capacity profile dict (potentially) includes these keys:
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
    "OfficeHoursMondayStart",
    "OfficeHoursMondayEnd",
    "OfficeHoursTuesdayStart",
    "OfficeHoursTuesdayEnd",
    "OfficeHoursWednesdayStart",
    "OfficeHoursWednesdayEnd"
    "OfficeHoursThursdayStart",
    "OfficeHoursThursdayEnd",
    "OfficeHoursFridayStart",
    "OfficeHoursFridayEnd",
    "OfficeHoursSaturdayStart",
    "OfficeHoursSaturdayEnd",
    "OfficeHoursSundayStart",
    "OfficeHoursSundayEnd"
    '''

    params = {
      'AlwaysReturnProfile': AlwaysReturnProfile
      }

    path = '/resource/{}/capacity/profiles'.format(ResourceId)

    return self._get(path, params=params)



  def get_costumers(self, costumer_id=None, **kwargs):
    '''
    Returns a single costumer if costumer_id is set.
    Returns all clients otherwise. Some fields can
    be supplied with values for filtering.
    '''

    if costumer_id:
      path = '/resource/customer/{}'.format(costumer_id)
    else:
      path = '/resource/customers'

    return self._get(path, params=kwargs)


  def get_companies(self, active=True):
    '''
    Get a list of companies
    Params: active
    '''

    path = '/core/resourcecompany'

    return self._get(path, params={'Active': active})

  def currency_convert(self, **kwargs) -> "Float":
    '''Convert an ammount from one currency to another.
    Either CurrencyTableId, CompanyId or JobId MUST be supplied!
    Returns the converted amount as a float

    Keyword arguments:
    Amount (Float): The amount to convert
    FromCurrencyId (Int): The ID of the currency of the amount to convert
    ToCurrencyId (Int): The ID of the currency to convert to
    PerDate (DateTime string): The date to use for currency conversion. Defaults to today if omitted.
    CurrencyTableId (Int): The currency table to get the exchange rate from. 
    CompanyId (Int): The ID of the company to get the exchange rate from (uses the currency table of the company).
    JobId (Int): The ID of the job to get the exchange rate from (uses the currency table of the company of the job)
    '''

    path = '/core/currency/convert'

    return self._get(path, params=kwargs)


  def get_creditors(self, **kwargs):
    '''
    Get a list of companies
    Implements: CreditorListsRequest
    '''

    #path = '/finance/accounts/creditors'
    path = '/finance/account/visualization/creditors'

    return self._get(path, params=kwargs)


  def get_currencies(self, reporting_currency:"Bool"=True, including_blocked:"Bool"=False) -> "List":
    '''
    Get a list of currencies
    Implements: CurrenciesRequest
    '''
    params = {
      "ReportingCurrency": reporting_currency,
      "IncludingBlocked": including_blocked
      }

    path = '/core/currencies'

    return self._get(path, params=params)


  def get_departments(self, **kwargs):
    '''
    Get a list of departments
    '''

    path = '/core/departments'

    return self._get(path, params=kwargs)


  def get_debtors(self, company_id=None, blocked=False, has_outstanding_amount=True):
    '''
    Get a list of debtors
    Params:
      CompanyId: Int
      Blocked: Bool
      HasOutstandingAmount: Bool
    '''
    # With this I get RemainingTotalAmount: CustomerDebtorsVisualizationRequest
    # /resource/customer/{CustomerId}/visualization/debtors/balance
    # But then I need the customerID

    params = {
      'CompanyId': company_id,
      'Blocked': blocked,
      'HasOutstandingAmount': has_outstanding_amount
      }

    path = '/finance/debtors'
    #path = '/finance/account/visualization/debtors'

    return self._get(path, params=params)


  def get_debtors_balance(self, company_id, blocked=False):
    '''
    Get balance for debtors
    Implements: DebtorsBalenceRequest
    Params:
      CompanyId: Int
      Blocked: Bool
    '''

    params = {
      'CompanyId': company_id,
      'Blocked': blocked
    }

    path = '/finance/debtors/visualization/balance'

    return self._get(path, params=params)


  def get_employees(self, **kwargs):
    '''Get a list of employees. Implements EmployeesRequest
    
    Keyword arguments:
    CompanyId (Int): Id of company to get employees for	
    Active (Bool): Only return active employees
    UserAccountTypes (List of ints): A list of account types to return
    
    Returns:
    Id (Int): Id of this employee. Matches a resource Id for same person
    EmployeeName (String): ?
    WeekendType (Int): ?
    WeekStart (Int): ?,
    CompanyId (Int): ?
    ReportProfileId (Int): ?,
    EmployeePosition (Int): ?,
    PriceGroupId (Int): ?,
    DisplayCurrencyId (Int): ?
    DepartmentId (Int): ?
    ExpiryDate (String) : "0001-01-01T00:00:00.000Z"
    DomainLoginName (String): ?
    Active (Bool): ?
    Birthday (String): "0001-01-01T00:00:00.000Z"
    DefaultActivityId (Int): ?
    ManagerResourceId (Int): ?
    TrafficManagerResourceId (Int): ?
    TimeSheetApproverResourceId (Int): ?
    SubstituteEmployeeId (Int): ?
    EmploymentTypeId (int): ?
    ReferenceKey (Int): ?
    ExternalCode (String): ?
    TimeRegistration (Bool): ?
    TimeRegistrationReceiveMail (Bool): ?
    Sex (Int): ?
    DocumentFormatStandard (Int): ?
    SystemSetting (String): ?
    Localtion (String): ?
    ReimbursementApproveManagerResourceId (Int): ?
    MailAlias (String): ?
    EmailBodyFormatType (Int):
    ExternalCalenderSync (Int): ?
    NewbizzResourceAccess (Bool): ?
    FlexProfileId (Int): ?
    AmountApproveVoucherJob (Int): ?
    AmountApproveVoucherNonJob (Int): ?
    AmountApproveRegulation (Int): ?
    AmountApproveWriteOff (Int): ?
    SystemLogOn (Bool): ?
    SystemLogOnTime (String): "0001-01-01T00:00:00.000Z"
    SystemLogOffTime (String): "0001-01-01T00:00:00.000Z"
    CloseDownSystem (Bool): ?
    EmployeeAccessProfileId (Int): ?
    DriveRegistrationNumberRefund (Bool): ?
    ExternalNumber (Int): ?
    UpdateResourceId (Int): ?
    UpdateDate (String): "0001-01-01T00:00:00.000Z"
    UpdateType (Int): ?
    AllowVendorInvoiceQuickRegistration (Bool): ?
    AllowVATEdit (Bool): ?
    FlexDisabled (Bool): ?
    AllowDebtorEdit (Bool): ?
    AllowCreditorEdit (Bool): ?
    AllowFinanceAccountEdit (Bool): ?
    ExchangeSyncStatus (Int): ?
    ExchangeSyncMethod (Int): ?
    ExchangeMailStatus (Int): ?
    ExchangeActiveFolder (String): ?
    BonusStandardShare (Int): ?
    ExchangeSyncFrequency (Int): ?
    LocationStatus (Int): ?
    FormattingLCID (Int): ?
    UDC1 (String): ?
    UDC2 (String): ?
    UDC3 (String): ?
    UDC4 (String): ?
    UDC5 (String): ?
    FollowUpRefresh (Int)" ?
    AllowExpenseEntry (Bool): ?
    HolidayCalendarId (Int): ?
    WorkDayAverageMethod (Int): ?
    OfficeId (Int): 0
    FullClientAccess (Bool): ?
    AllowCreateTags (Bool): ?
    AllowCreateSkills (Bool): ?
    AllowSaveNewJobTemplates (Bool): ?
    PermanentlyDisabled (Bool): ?
    '''

    path = '/resource/employees'

    return self._get(path, params=kwargs)


  def get_employee(self, **kwargs):
    '''
    Get a single employee
    '''
    assert 'Id' in kwargs.keys()

    path = '/resource/employee/{}'.format(kwargs['Id'])

    return self._get(path, params=kwargs)


  def get_employee_positions(self):
    '''
    Get a employee positions
    Implements: EmployeePositionsRequest
    '''

    path = '/resource/employee/positions'

    return self._get(path, params={})


  def get_invoices(self, status=[], job_id=None, customer_id=None):
    '''
    Get a list of invoices for job_id
    Params:
      status: List of status IDs
    '''

    # If int supplied, put it into a list
    if type(status) == int:
      status = [status]

    params = {
      'Status': status,
      'JobId': job_id,
      'CustomerId': customer_id
      }

    # Status must be a list
    assert isinstance(status, list), "status must be a list in get invoices()"

    path = "/job/invoices"

    return self._get(path, params)


  def get_invoice_types(self, **kwargs):
    '''
    Get invoice types
    '''

    path = '/job/invoice/virtualization/types'

    return self._get(path, params=kwargs)


  def get_jobs(self, **kwargs):
    '''Returns a list of jobs.

    Keyword arguments:
    Status (List of ints): FIlter on status ids of the jobs.
    TicketEnabled (Bool): Filter on whether tickets is enabled on that job or not.
    StartDate (String): Filter on job start date.
    EndDate (String): Filter on job end date.
    CreateDate (String): Filter on job create date.
    ExpenditureAccountMethodIds: (List of ints): Filter on expenditures account method ids selected on the jobs.
    JobIds (List of ints): Filter on specific job ids. Useful when checking if the job matches the filter.
    VoucherRegistrationAllowed (Bool): Filter on voucher registration allowed on job.
    CompanyId (Int): Filter on job company id.
    ProjectId (Int): Filter on job project id.
    PipelineIds (List of ints): Filter on specific pipeline ids
    CustomerTypes (List of int): Filter on customer types
    '''
    # FIXME: Add path argument ResourceID or make get_job(id)

    if 'Status' in kwargs:
      assert isinstance(kwargs['Status'], list), "Status must be a list"

    path = '/jobs'

    return self._get(path, params=kwargs)


  def get_job_types(self, **kwargs):
    '''
    Params:
      Active (Bool): Filter on active/inactive jobs 
      CompanyId (Int): ID of company to get job types for
    '''
    if 'Active' in kwargs:
      assert isinstance(kwargs['Active'], bool), "Active must be a bool"

    if 'CompanyId' in kwargs:
      assert isinstance(kwargs['CompanyId'], bool), "CompanyId must be an int"

    path = '/settings/job/types'

    return self._get(path, params=kwargs)


  def get_job(self, **kwargs):
    '''
    Get a single job
    '''
    assert 'Id' in kwargs.keys()

    path = '/job/{}'.format(kwargs['Id'])

    return self._get(path, params=kwargs)


  def get_projects(self, **kwargs):
    '''
    Get a list of projects.
    Params:
      customer_id: Projects for a single customer
    '''

    if 'customer_id' in kwargs:
      path = '/resource/customer/' + str(customer_id) + '/projects' 
    else:
      path = '/projects'

    return self._get(path, params=kwargs)


  def get_resources(self, **kwargs):
    '''
    Get at list of resources (People)
    TypeID:
      2 = Employee
      10 = Contact
    '''

    path = '/resources'

    return self._get(path, params=kwargs)


  def get_resource(self, **kwargs):
    '''
    Get a single resource
    '''
    assert 'Id' in kwargs.keys()

    path = '/resource/{}'.format(kwargs['Id'])

    return self._get(path, params=kwargs)


  def get_time_entries(self, **kwargs):
    '''
    Get a list of time entries covering work done
    between Start and End
    Implements: RawTimeEntriesRequest
    
    Keyword arguments:
    ResourceId (Int): Resource id, fallback to current if nothing is set.
    Start (String): Start date
    End (String): End date
    TaskId (Int): Task Id
    JobId(Int): Job Id
    ApprovalStatus (Int): Approval Status
    JournalNumber (Int): Journal Number
    HasTimeRegistration (Bool): Has Time Registration
    SequenceNumber (List)(Int): Sequence Number
    
    Returns (some of) these:
    Id (Int),
    ResourceId (Int),
    JobId (Int),
    TaskId (Int),
    ActivityId (Int),
    Hours (Float),
    Description (String),
    DescriptionRequired (Bool),
    Cost (Float),
    Sale (Float),
    CostMethod (Int?),
    SaleMethod (int?)
    SequenceNumber (Int?),
    JournalNumber (Int),
    Correction (Int?),
    CorrectionJob (Int?)
    ,"CorrectionCost":0,
    "CorrectionSale":0,
    "SaleOriginal":0,
    "EmployeeHolidayRecordId":0,
    "PayrollJournalId":0,
    "HoursMoved":0,
    "ICSale":0,
    "CorrectionNote":"String",
    "CorrectionDate":"0001-01-01T00:00:00.000Z",
    "CorrectionReferenceId":0,
    "CorrectionOrgDate":"0001-01-01T00:00:00.000Z",
    "Public":false,
    "CorrectionResId":0,
    "PartInvoiceRefInvId":0,
    "PricelistId":0,
    "CostCurrencyId":0,
    "SaleCurrencyId":0,
    "CostCurrencyAmount":0,
    "SaleCurrencyAmount":0,
    "ApprovalEmployeeResourceId":0,
    "ApprovalEmployeeDate":"0001-01-01T00:00:00.000Z",
    "ApprovalProjectManagerResourceId":0,
    "ApprovalProjectManagerDate":"0001-01-01T00:00:00.000Z",
    "ApprovalAdminResourceId":0,
    "ApprovalAdminDate":"0001-01-01T00:00:00.000Z",
    "ApprovalRejectResourceId":0,
    "ApprovalRejectComment":"String",
    "ApprovalRejectDate":"0001-01-01T00:00:00.000Z",
    "ApprovalStatus":0,
    "Billable":false,
    "InternalDescription":"String",
    "MaxPerEntry":0,
    "MaxPerEntryCurrency":0,
    "PriceAdjustmentID":0,
    "PriceAdjustmentChangeDate":"0001-01-01T00:00:00.000Z",
    "PriceAdjustmentSaleRate":0,
    "PriceAdjustmentCostRate":0,
    "SaleOriginAmount":0,
    "CostOriginAmount":0,
    "UpdateResourceId":0,
    "UpdateComment":"String",
    "UpdateDate":"0001-01-01T00:00:00.000Z",
    "UpdateType":0,
    "HasApprovedResourceInitals":"String",
    "HasApprovedNotResourceInitals":"String",
    "TariffId":0,
    "TariffAdditionalPercentCost":0,
    "TariffAdditionalPercentSale":0,
    "TariffAdditionalPercentIcSale":0,
    "Underposting":"0001-01-01T00:00:00.000Z",
    "DeletedMarked":false,
    "CreateDate":"0001-01-01T00:00:00.000Z",
    "CreateResourceId":0
    '''

    path = '/personalexpense/timeentries/raw'

    return self._get(path, params=kwargs)




  def get_expense_entries(self, **kwargs):
    '''
    Get at list of price quotes
    '''

    path = '/personalexpense/expenseentries'

    return self._get(path, params=kwargs)


  def get_employee_price_groups(self, show_inactive=False):
    '''
    Get at list of employee price groups
    Implements: EmployeePriceGroupsRequest
    '''
    params = {
      'ShowInactive': show_inactive
      }

    path = '/settings/employee/pricegroups'

    return self._get(path, params=params)


  def get_employee_prices_hour(self, **kwargs):
    """Get at list of employee prices hour. Employees can have more
    than one entry, because prices can change (Be added) over time.
    
    Keyword arguments:
    EmployeeId (Int): ID of Employee to get prices per hour for
    ValidFrom (Date string): For when the price per hour is valid from
    EmployeePosition (Int): To get employees for a specific position
    PriceGroupId (Int): To get employees for a specific price group
    ActiveEmployees (Bool): Show active/inactive employees. Show both if null/not provided
    
    Returns (Some of):
    Id (Int): ID of prices
    EmployeeId (Int): Id of employee
    HoursCost (Float): ?
    Profit (Float): ?
    HoursSale (Float): ?
    CurrencyId (Int): Id of currency
    ICSale (Float): ?
    """
    path = '/settings/employee/priceshour'

    return self._get(path, params=kwargs)
