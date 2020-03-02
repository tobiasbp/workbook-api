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
    """
    Args:
      path: The string added to the base URL
      params: key,value pairs to send in URL
    """
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


  def get_departments(self, **kwargs):
    '''
    Get a list of departments
    '''

    path = '/core/departments'

    return self._get(path, params=kwargs)


  def get_employees(self, **kwargs):
    '''
    Get a list of employees
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


  def get_jobs(self, **kwargs):
    '''
    Params:
      Status: Jobs returned must match these statii
    '''
    if 'Status' in kwargs:
      assert isinstance(kwargs['Status'], list), "Status must be a list"

    path = '/jobs'

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


  def get_expense_entries(self, **kwargs):
    '''
    Get at list of price quotes
    '''

    path = '/personalexpense/expenseentries'

    return self._get(path, params=kwargs)


  def get_employee_price_groups(self, **kwargs):
    '''
    Get at list of employee price groups
    '''

    path = '/settings/employee/pricegroups'

    return self._get(path, params=kwargs)


  def get_employee_prices_hour(self, **kwargs):
    '''
    Get at list of employee prices hour
    '''

    assert 'Id' in kwargs

    path = '/settings/employee/priceshour/current'

    return self._get(path, params=kwargs)
