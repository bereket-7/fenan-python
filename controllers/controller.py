class Controller(BaseController):
    def __init__(self):
        super().__init__()

    def authorize_request(self, ability, arguments=[]):
        self.authorize(ability, arguments)

    def dispatch_job(self, job):
        self.dispatch(job)

    def validate_request(self, request, rules):
        self.validate(request, rules)
