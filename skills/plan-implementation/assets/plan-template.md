# Implementation plan: {{feature_title}}

<!-- Authoring notes: replace every {{placeholder}} and remove these notes.
Adapt sections to the size of the change. Remove optional sections that do not
apply; retain explicit statements where the skill requires them, such as no
schema changes. Build links relative to the output document. Do not claim
approval or successful checks without evidence. -->

Feature id: {{stable_kebab_case_id}}
Status: {{actual_plan_status_and_blocking_decisions}}
Updated: {{date_of_this_revision}}
Requirements: {{link_to_existing_specification_or_requirement_source}}

## Objective and scope

{{brief_objective_expected_behavior_example_and_scope_boundaries}}

{{acceptance_ids_in_scope_without_duplicating_the_specification}}

## Current state and evidence

{{inspected_paths_symbols_callers_and_relevant_data_flow}}

{{verified_facts_distinguished_from_inferences_and_proposed_new_components}}

## Approach and decisions

{{recommended_approach_responsibilities_inputs_outputs_and_error_handling}}

<!-- Compare alternatives only when they affect a material decision. -->
{{viable_alternatives_tradeoffs_rationale_and_conditions_for_reconsideration}}

{{agreed_decisions_and_decisions_still_needed}}

## File and contract impact

| Existing or proposed path | Action | Symbol or responsibility | Change and rationale | Affected consumers or contracts |
| --- | --- | --- | --- | --- |
| {{path_and_whether_existing_or_proposed}} | {{add_modify_or_remove}} | {{symbol_or_responsibility}} | {{behavior_change_and_reason}} | {{affected_contracts}} |

## Models and data

<!-- If no schema changes are needed, state that and remove the table.
Otherwise include every affected attribute and the model's responsibility. -->

{{model_responsibilities_or_explicit_no_schema_change_statement}}

| Model and file | Attribute | Current to proposed definition | Type and parameters | Nullability, defaults, validation | Relationships, indexes, constraints | Existing data treatment and rationale |
| --- | --- | --- | --- | --- | --- | --- |
| {{model_and_path}} | {{attribute}} | {{definition_change}} | {{type_and_parameters}} | {{validation_and_defaults}} | {{relationships_and_constraints}} | {{data_compatibility_conversion_and_reason}} |

<!-- Optional when schema or stored data changes. Describe, do not execute. -->
{{migration_sequence_compatibility_locking_risks_and_recovery}}

## Implementation sequence

{{ordered_steps_with_dependencies_affected_files_outcomes_and_acceptance_ids}}

<!-- Keep design sequencing here. Create a separate tasks.md only when task
breakdown is requested; execution status belongs in that document. -->

## Verification

| Acceptance criterion or risk | Scenario and level of check | Proposed command or procedure | Expected result |
| --- | --- | --- | --- |
| {{criterion_or_risk}} | {{scenario_and_check_level}} | {{project_specific_command_or_procedure}} | {{observable_success_condition}} |

{{checks_actually_performed_during_investigation_and_their_results_or_none}}

{{checks_pending_implementation_and_any_execution_limitations}}

## Risks and recovery

{{concrete_risks_mitigations_and_compatibility_concerns}}

<!-- Include rollout, rollback, and data recovery only when relevant. -->
{{proportional_rollout_and_recovery_approach_with_irreversible_steps_identified}}

## Assumptions and open questions

{{remaining_assumptions_questions_their_impact_and_next_investigation_or_none}}
