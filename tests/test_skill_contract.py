from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
SKILL_ROOT = ROOT / "skills" / "digital-employee-builder"


class SkillContractTests(unittest.TestCase):
    def read(self, relative: str) -> str:
        return (SKILL_ROOT / relative).read_text(encoding="utf-8")

    def test_discovery_description_is_trigger_only_and_concise(self):
        text = self.read("SKILL.md")
        frontmatter = text.split("---", 2)[1]
        match = re.search(r'^description:\s*["\']?(.+?)["\']?$', frontmatter, re.MULTILINE)
        self.assertIsNotNone(match)
        description = match.group(1)
        self.assertTrue(description.startswith("Use when "))
        self.assertLess(len(description), 500)

    def test_entrypoint_is_a_progressive_router(self):
        text = self.read("SKILL.md")
        self.assertLess(len(text), 15000)
        for reference in (
            "references/conversation-protocol.md",
            "references/migration-analysis.md",
            "references/embedded-runtime.md",
        ):
            self.assertIn(reference, text)
            self.assertTrue((SKILL_ROOT / reference).is_file())

    def test_role_modeling_is_a_required_progressive_reference(self):
        skill = self.read("SKILL.md")
        self.assertIn("references/role-modeling.md", skill)
        reference = self.read("references/role-modeling.md").lower()
        for concept in (
            "source evidence",
            "employee role brief",
            "success outcomes",
            "decision authority",
            "specificity test",
            "file responsibility map",
        ):
            self.assertIn(concept, reference)

    def test_agents_template_is_an_operational_contract(self):
        text = self.read("assets/workspace/AGENTS.md.tmpl")
        for section in (
            "## Mission and Outcomes",
            "## Success Criteria",
            "## Operating Loop",
            "## Decision Authority",
            "## Capability Map",
            "## Approval Protocol",
            "## Evidence and Reporting",
            "## Failure and Recovery",
            "## Memory and Data Handling",
        ):
            self.assertIn(section, text)

    def test_soul_template_encodes_professional_judgment_and_behavior(self):
        text = self.read("assets/workspace/SOUL.md.tmpl")
        for section in (
            "## Professional Identity",
            "## Purpose",
            "## Domain Expertise",
            "## Judgment Principles",
            "## Communication Style",
            "## Scenario Behavior",
            "## Professional Boundaries",
        ):
            self.assertIn(section, text)
        self.assertNotIn("Pick one of these baselines", text)

    def test_identity_template_is_compact_but_substantive(self):
        text = self.read("assets/workspace/IDENTITY.md.tmpl")
        for field in (
            "**Name**",
            "**Role**",
            "**Organization**",
            "**Mandate**",
            "**Serves**",
            "**Accountable outcomes**",
            "**Core expertise**",
            "**Signature**",
        ):
            self.assertIn(field, text)
        self.assertNotIn("**Vibe**", text)

    def test_conversation_batches_questions_and_uses_risk_gates(self):
        text = self.read("references/conversation-protocol.md")
        self.assertIn("at most three", text.lower())
        self.assertIn("risk gate", text.lower())
        self.assertIn("delta", text.lower())
        self.assertIn("normal gate first", text.lower())
        self.assertIn("same reply", text.lower())

    def test_migration_analysis_classifies_source_modules(self):
        text = self.read("references/migration-analysis.md").lower()
        for decision in ("preserve", "adapt", "replace", "externalize", "drop"):
            self.assertIn(decision, text)
        self.assertIn("user task", text)
        self.assertIn("source tests", text)
        for cutover_term in ("cutover", "rollback", "integrity", "delta"):
            self.assertIn(cutover_term, text)

    def test_embedded_runtime_is_single_source_of_business_behavior(self):
        text = self.read("references/embedded-runtime.md").lower()
        self.assertIn("single source", text)
        self.assertIn("local mcp", text)
        self.assertIn("external adapter", text)
        self.assertNotIn("one capability point = one mcp tool", self.read("SKILL.md").lower())

    def test_python_mcp_template_calls_local_runtime_without_http_client(self):
        text = self.read("assets/mcp-server-python/server.py.tmpl")
        self.assertIn("employee_runtime", text)
        self.assertNotIn("import httpx", text)
        self.assertNotIn("BUSINESS_API_BASE", text)

    def test_workflow_template_reuses_shared_runtime(self):
        text = self.read("assets/skill-template/scripts/workflow.py.tmpl")
        self.assertIn("employee_runtime", text)
        self.assertNotIn("def api(", text)
        self.assertNotIn("BUSINESS_API_BASE", text)

    def test_python_embedded_runtime_asset_has_package_and_tests(self):
        required = (
            "assets/embedded-runtime-python/pyproject.toml.tmpl",
            "assets/embedded-runtime-python/src/employee_runtime/application.py.tmpl",
            "assets/embedded-runtime-python/src/employee_runtime/ports.py.tmpl",
            "assets/embedded-runtime-python/src/employee_runtime/adapters/sqlite_repository.py.tmpl",
            "assets/embedded-runtime-python/src/employee_runtime/adapters/sqlite_execution_store.py.tmpl",
            "assets/embedded-runtime-python/tests/test_application.py.tmpl",
        )
        for relative in required:
            self.assertTrue((SKILL_ROOT / relative).is_file(), relative)

    def test_runtime_ports_model_dependency_audit_and_idempotency(self):
        text = self.read("assets/embedded-runtime-python/src/employee_runtime/ports.py.tmpl")
        for contract in ("DependencyError", "AuditSink", "IdempotencyStore"):
            self.assertIn(contract, text)

    def test_mcp_templates_cover_write_safety_and_dependency_errors(self):
        python_text = self.read("assets/mcp-server-python/server.py.tmpl")
        self.assertIn("DependencyError", python_text)
        typescript_text = self.read("assets/mcp-server-ts/server.ts.tmpl")
        self.assertIn("idempotencyKey", typescript_text)
        self.assertIn("dryRun", typescript_text)
        self.assertIn("{{write_task}}", typescript_text)
        query_handler = typescript_text.split('"{{write_task}}"', 1)[0]
        self.assertIn("error instanceof DependencyError", query_handler)

    def test_harness_setup_template_installs_and_verifies_runtime(self):
        text = self.read("assets/workspace/harness-setup.md.tmpl").lower()
        self.assertIn("runtime", text)
        self.assertIn("clean environment", text)
        self.assertIn("tools/list", text)

    def test_openclaw_reference_registers_and_probes_local_mcp(self):
        text = self.read("references/openclaw-workspace.md")
        self.assertIn("mcp.servers", text)
        self.assertIn("openclaw mcp doctor", text)


if __name__ == "__main__":
    unittest.main()
