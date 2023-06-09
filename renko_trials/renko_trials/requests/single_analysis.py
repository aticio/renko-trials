class SingleAnalysisCreateInvalidRequest:
    def __init__(self):
        self.errors = []

    def add_error(self, param, message):
        self.errors.append({"parameter": param, "message": message})

    def has_errors(self):
        return len(self.errors) > 0

    def __bool__(self):
        return False


class SingleAnalysisCreateValidRequest:
    def __init__(self, parameters=None):
        self.parameters = parameters

    def __bool__(self):
        return True


def build_single_analysis_request(parameters=None):
    accepted_parameters = ["symbol", "percent", "repo", "start_date", "end_date"]
    invalid_req = SingleAnalysisCreateInvalidRequest()

    if parameters is not None:
        if not isinstance(parameters, dict):
            invalid_req.add_error("parameters", "Is not iterable")
            return invalid_req

        if len(parameters) != 5:
            invalid_req.add_error("parameters", "missing parameter")
            return invalid_req

        for key, value in parameters.items():
            if key not in accepted_parameters:
                invalid_req.add_error(key, "Key {} cannot be used".format(key))
                return invalid_req
    else:
        invalid_req.add_error("", "Need 5 parameters, got 0")
        return invalid_req

    return SingleAnalysisCreateValidRequest(parameters=parameters)
