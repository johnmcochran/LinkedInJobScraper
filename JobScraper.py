import bs4

class JobScraper:
    '''
    pass criteria as dictionary with values formatted as:
        {
            job title/description: value (e.g. data engineer)
            remote: value e.g. hybrid
            minimum salary: value
            etc.
        }
    pass exclusion_criteria as dictionary with values formatted as:
        {

        }
    by calling JobsBoard(criteria, exclusion_criteria)
    '''
    def __init__(self, query_criteria, exclusion_criteria = None):
        self.query_criteria = query_criteria
        self.jobsUrl = 'https://www.linkedin.com/jobs/search'
        self.jobsHtml = None
        self.jobs = None

    def __buildQuery(self):
        query_string = '/?'
        for k,v in self.query_criteria:
            query_string+= k + '=' + v + '&'
        query_string = query_string[:-1]

    def __queryJobs(self, criteria: dict):
        # self.jobsHtml =
        return None

    def __parseJobs(self):
        # self.jobs =
        # return __filterJobs(self.jobs)
        return None

    def __filterJobs(self, exclusion_criteria: dict):
        if exclusion_criteria is None:
            return self.jobs
        for job in self.jobs:
            for k,v in exclusion_criteria:
                if job[k] == v:
                    self.jobs.remove(job)
    def getJobs(self):
        return self.jobs


