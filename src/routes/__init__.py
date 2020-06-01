from tornado.routing import RuleRouter, Rule, PathMatches
from .api import api_app


router = RuleRouter([
  Rule(PathMatches("/api.*"), api_app("/api")),
])
