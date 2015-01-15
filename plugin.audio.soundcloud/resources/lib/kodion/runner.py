__author__ = 'bromix'

__all__ = ['run']

from .impl import Runner
from .impl import Context

__RUNNER__ = Runner()


def run(provider, context=None):
    if not context:
        context = Context()
        pass

    context.log_notice('Starting Kodion framework by bromix...')
    version = context.get_system_version()
    context.log_notice('System: %s' % version)
    context.log_notice('Context: %s (%s)' % (context.get_name(), context.get_version()))
    __RUNNER__.run(provider, context)
    context.log_notice('Shutdown of Kodion')
    pass
