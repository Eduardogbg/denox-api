from tornado.routing import RuleRouter, Rule, PathMatches
from .api import api_app


def router(params): 
  return RuleRouter([
    Rule(PathMatches("/api.*"), api_app("/api", params)),
  ])
