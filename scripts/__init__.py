"""Scripts package for the Unified Developer Workflow.

This package contains automation scripts for:
- Project generation and bootstrapping
- Brief processing and planning
- Workflow automation and orchestration
- Compliance validation
- Deployment and rollback operations
- Testing and coverage collection
"""

# Export commonly used modules to simplify imports
from . import lifecycle_tasks

__all__ = ['lifecycle_tasks']
