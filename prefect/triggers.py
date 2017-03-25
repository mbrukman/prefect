"""
Triggers are functions that determine whether a task should run.

Triggers are passed the task in question and a sequence of states from
preceding tasks. Triggers raised TriggerFailed is they fail and return None
otherwise.
"""
import prefect.exceptions
from prefect.state import State

def all_success(task, preceding_states):
    if not all([s == State.SUCCESS for s in preceding_states]):
        raise prefect.exceptions.TriggerFailed(
            'All success: not all tasks succeeded')

def all_failed(task, preceding_states):
    if not all([s == State.FAILED for s in preceding_states]):
        raise prefect.exceptions.TriggerFailed(
            'All failed: not all tasks failed')

def any_success(task, preceding_states):
    if not any([s == State.SUCCESS for s in preceding_states]):
        raise prefect.exceptions.TriggerFailed(
            'Any success: no tasks succeeded')

def any_failed(task, preceding_states):
    if not any([s == State.FAILED for s in preceding_states]):
        raise prefect.exceptions.TriggerFailed(
            'Any failed: no tasks failed')