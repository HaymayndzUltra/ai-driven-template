# Phase 6: Operations

## AI Role
**Operations Engineer** - Monitor and maintain production systems

## Mission
Maintain SLO compliance, track updates, and conduct retrospectives/postmortems for continuous improvement and operational excellence.

## Prerequisites
- Phase 5 completed (Retrospective finished)
- Production systems deployed
- Monitoring and alerting configured

## Process

### 1. SLO Monitoring and Compliance
- **Monitor Service Level Objectives**: Track key metrics and thresholds
- **Alert Management**: Respond to SLO breaches and anomalies
- **Performance Tracking**: Monitor system performance and resource utilization
- **User Experience Monitoring**: Track user satisfaction and feedback

### 2. Incident Management
- **Incident Detection**: Identify and classify incidents by severity
- **Response Coordination**: Coordinate response teams and stakeholders
- **Root Cause Analysis**: Investigate and document root causes
- **Postmortem Conduct**: Conduct postmortems for significant incidents
- **Action Items**: Track and implement postmortem action items

### 3. Continuous Improvement
- **Dependency Updates**: Track and apply security and dependency updates
- **Performance Optimization**: Identify and implement performance improvements
- **Capacity Planning**: Monitor capacity and plan for growth
- **Process Refinement**: Improve operational processes based on learnings

### 4. Documentation and Knowledge Management
- **Runbook Updates**: Maintain and update operational runbooks
- **Knowledge Base**: Document operational procedures and lessons learned
- **Training Materials**: Create and maintain training documentation
- **Best Practices**: Document and share operational best practices

## Operational Activities

### Daily Operations
- **Health Checks**: Verify system health and functionality
- **Metric Review**: Review key performance indicators
- **Alert Triage**: Review and triage alerts
- **Capacity Monitoring**: Monitor resource utilization

### Weekly Operations
- **SLO Review**: Review SLO compliance and trends
- **Incident Review**: Review incidents and response effectiveness
- **Performance Analysis**: Analyze performance trends and bottlenecks
- **Dependency Updates**: Review and apply dependency updates

### Monthly Operations
- **Postmortem Analysis**: Conduct postmortems for significant incidents
- **Capacity Planning**: Review capacity and plan for growth
- **Process Improvement**: Identify and implement process improvements
- **Training Updates**: Update training materials and procedures

### Quarterly Operations
- **Strategic Review**: Review operational strategy and objectives
- **Technology Assessment**: Assess technology stack and alternatives
- **Team Development**: Plan team development and training
- **Budget Planning**: Plan operational budget and resources

## Outputs

### Monitoring Dashboards
- **SLO Dashboard**: Real-time SLO compliance and metrics
- **Performance Dashboard**: System performance and resource utilization
- **Incident Dashboard**: Incident status and response metrics
- **User Experience Dashboard**: User satisfaction and feedback metrics

### Incident Reports
- **Incident Summary**: Brief description and impact
- **Timeline**: Detailed incident timeline and response
- **Root Cause**: Analysis of root cause and contributing factors
- **Action Items**: Specific actions to prevent recurrence

### Postmortem Reports
- **Incident Overview**: Summary of incident and impact
- **Timeline Analysis**: Detailed timeline of events
- **Root Cause Analysis**: Deep dive into root causes
- **Lessons Learned**: Key insights and improvements
- **Action Plan**: Specific actions and timeline

### Operational Documentation
- **Runbooks**: Step-by-step operational procedures
- **Knowledge Base**: Operational knowledge and best practices
- **Training Materials**: Training documentation and resources
- **Best Practices**: Documented operational best practices

## Quality Gates

### Validation Checkpoints
- [ ] SLO monitoring configured and operational
- [ ] Incident response procedures documented
- [ ] Postmortem process established
- [ ] Continuous improvement process active
- [ ] Documentation maintained and current

### Success Criteria
- SLO compliance maintained above thresholds
- Incidents resolved within target timeframes
- Postmortems conducted for significant incidents
- Continuous improvement actions implemented
- Operational knowledge documented and accessible

## Duration
**Target**: Ongoing  
**Actual**: Continuous operational activities

## Next Phase
Return to **Phase 0: Bootstrap** for new features or improvements

## Automation Integration

### AI Actions
```python
# Operations execution
def execute_operations(production_systems, monitoring_config):
    # 1. Monitor SLOs
    slo_status = monitor_slo_compliance(production_systems)
    
    # 2. Detect incidents
    incidents = detect_incidents(slo_status, monitoring_config)
    
    # 3. Respond to incidents
    for incident in incidents:
        response = coordinate_incident_response(incident)
        root_cause = analyze_root_cause(incident)
        postmortem = conduct_postmortem(incident, root_cause)
    
    # 4. Continuous improvement
    improvements = identify_improvement_opportunities(slo_status, incidents)
    
    # 5. Update documentation
    update_operational_docs(improvements, postmortems)
    
    # 6. Log evidence
    log_evidence("phase6", slo_status, incidents, improvements)
    
    return {
        "slo_status": slo_status,
        "incidents": incidents,
        "improvements": improvements,
        "evidence": get_evidence("phase6")
    }
```

### Human Validation
- User reviews SLO compliance
- User approves incident response
- User validates postmortem findings
- User confirms improvement actions

## Error Handling

### Common Issues
- **SLO breaches**: Immediate response required
- **Incident escalation**: Coordinate with appropriate teams
- **Documentation gaps**: Update documentation immediately

### Recovery Actions
- Escalate critical incidents immediately
- Conduct postmortem for significant incidents
- Update procedures based on learnings
- Implement preventive measures

## Automation Integration
- Monitor live SLOs using `Phase6OperationsWrappers.monitor_slo(project, availability=..., latency=..., error_rate=...)`. The
  wrapper records PASS/FAIL state in both the manifest and validation log.
- Schedule retrospectives with `Phase6OperationsWrappers.schedule_retros(project, start=..., cadence=..., count=...)` to generate
  the retro cadence JSON file.

## Evidence Templates
- Operations templates such as retro agendas and postmortem shells align with the phase 6 entries in
  [workflow1_evidence/index.json](../templates/workflow1_evidence/index.json).

## Operator Instructions
- Capture operational incidents in `postmortem_template` outputs and set `automation.parameters` fields to include incident IDs.
- When SLO checks fail, escalate by annotating the validation report with `automation_enforced: false` for the impacted phase and
  attach any manual evidence collected outside the wrapper.
