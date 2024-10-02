class GraphQlShell:

    def __init__(self, query=None, variables=None):
        self.query = query
        self.variables = variables

    def get_query(self):
        return self.query

    def set_query(self, query):
        self.query = query

    def get_variables(self):
        return self.variables

    def set_variables(self, variables):
        self.variables = variables

    def __str__(self):
        return f"query={self.query}, variables={self.variables}"