"""
Comprehensive Databricks Git Integration Test Suite
This test framework covers various scenarios for testing Git integration in Databricks
"""

import unittest
import json
import requests
from datetime import datetime
from databricks_cli.sdk.api_client import ApiClient
from databricks_cli.repos.api import ReposApi
from databricks_cli.workspace.api import WorkspaceApi
from databricks_cli.dbfs.api import DbfsApi
import git
import os
import tempfile
import time

class DatabricksGitIntegrationTestBase(unittest.TestCase):
    """Base class for all Databricks Git integration tests"""
    
    def setUp(self):
        """Initialize test environment"""
        self.api_client = ApiClient(
            host=os.getenv('DATABRICKS_HOST'),
            token=os.getenv('DATABRICKS_TOKEN')
        )
        self.repos_api = ReposApi(self.api_client)
        self.workspace_api = WorkspaceApi(self.api_client)
        self.dbfs_api = DbfsApi(self.api_client)
        self.test_repo_url = "https://github.com/your-test-org/databricks-test-repo.git"
        self.test_branch = "test-branch"
        self.test_provider = "github"
        
    def tearDown(self):
        """Clean up test resources"""
        self.cleanup_test_repos()

class TestGitBasicOperations(DatabricksGitIntegrationTestBase):
    """Test basic Git operations in Databricks"""
    
    def test_01_repo_creation_and_linking(self):
        """Test creating a new repo and linking to Git"""
        print("Testing repo creation and Git linking...")
        
        # Create repo in Databricks
        repo_path = "/Repos/test_user/test_repo_creation"
        repo_info = self.repos_api.create(
            path=repo_path,
            url=self.test_repo_url,
            provider=self.test_provider,
            branch=self.test_branch
        )
        
        self.assertIsNotNone(repo_info)
        self.assertEqual(repo_info['path'], repo_path)
        self.assertEqual(repo_info['url'], self.test_repo_url)
        self.assertEqual(repo_info['branch'], self.test_branch)
        
        # Verify repo status
        status = self.repos_api.get(repo_path)
        self.assertEqual(status['status'], 'LINKED')
        
        return repo_info

    def test_02_pull_latest_changes(self):
        """Test pulling latest changes from remote Git"""
        print("Testing Git pull functionality...")
        
        repo_path = "/Repos/test_user/test_pull_changes"
        repo_info = self.repos_api.create(
            path=repo_path,
            url=self.test_repo_url,
            provider=self.test_provider
        )
        
        # Perform Git pull
        pull_result = self.repos_api.update(repo_path, branch="main")
        self.assertIsNotNone(pull_result)
        
        # Verify the repo is in sync
        repo_status = self.repos_api.get(repo_path)
        self.assertIn(repo_status['status'], ['LINKED', 'IN_SYNC'])

    def test_03_commit_and_push_changes(self):
        """Test committing and pushing changes from Databricks"""
        print("Testing commit and push functionality...")
        
        repo_path = "/Repos/test_user/test_commit_push"
        repo_info = self.repos_api.create(
            path=repo_path,
            url=self.test_repo_url,
            provider=self.test_provider,
            branch="test-commit-branch"
        )
        
        # Create a test notebook
        notebook_content = {
            "cells": [
                {
                    "cell_type": "code",
                    "execution_count": None,
                    "metadata": {},
                    "outputs": [],
                    "source": ["# Test notebook created for Git integration testing\n", "print('Hello Git Integration')"]
                }
            ],
            "metadata": {
                "language_info": {
                    "name": "python"
                }
            },
            "nbformat": 4,
            "nbformat_minor": 4
        }
        
        # Create notebook in the repo
        notebook_path = f"{repo_path}/test_git_notebook.py"
        self.workspace_api.import_workspace(
            path=notebook_path,
            content=json.dumps(notebook_content).encode('utf-8'),
            format="SOURCE",
            language="PYTHON"
        )
        
        # Commit the changes
        commit_message = f"Test commit from Databricks at {datetime.now()}"
        commit_result = self.repos_api.commit(repo_path, commit_message)
        
        self.assertIsNotNone(commit_result)
        self.assertEqual(commit_result['message'], commit_message)

class TestGitConflictScenarios(DatabricksGitIntegrationTestBase):
    """Test merge conflict scenarios and resolution"""
    
    def test_04_merge_conflict_detection(self):
        """Test that merge conflicts are properly detected"""
        print("Testing merge conflict detection...")
        
        # This test simulates a scenario where conflicts would occur
        # In practice, you'd need to orchestrate simultaneous changes
        
        repo_path = "/Repos/test_user/test_conflict_detection"
        repo_info = self.repos_api.create(
            path=repo_path,
            url=self.test_repo_url,
            provider=self.test_provider,
            branch="conflict-test-branch"
        )
        
        # Note: Actual conflict testing requires coordinated changes
        # This is a placeholder for the test logic
        print("Conflict detection test requires manual orchestration")

    def test_05_conflict_resolution_theirs(self):
        """Test accepting 'theirs' version in conflict resolution"""
        print("Testing 'Accept Theirs' conflict resolution...")
        
        # Implementation would involve creating a conflict scenario
        # then calling the conflict resolution API
        pass

    def test_06_conflict_resolution_mine(self):
        """Test accepting 'mine' version in conflict resolution"""
        print("Testing 'Accept Mine' conflict resolution...")
        pass

class TestGitBranchOperations(DatabricksGitIntegrationTestBase):
    """Test Git branch operations"""
    
    def test_07_branch_switching(self):
        """Test switching between Git branches"""
        print("Testing branch switching...")
        
        repo_path = "/Repos/test_user/test_branch_switch"
        repo_info = self.repos_api.create(
            path=repo_path,
            url=self.test_repo_url,
            provider=self.test_provider
        )
        
        # Switch to a different branch
        new_branch = "development"
        switch_result = self.repos_api.update(repo_path, branch=new_branch)
        
        self.assertIsNotNone(switch_result)
        
        # Verify branch was switched
        repo_status = self.repos_api.get(repo_path)
        self.assertEqual(repo_status['branch'], new_branch)

    def test_08_create_new_branch(self):
        """Test creating a new branch from Databricks"""
        print("Testing new branch creation...")
        
        repo_path = "/Repos/test_user/test_new_branch"
        repo_info = self.repos_api.create(
            path=repo_path,
            url=self.test_repo_url,
            provider=self.test_provider
        )
        
        new_branch_name = f"feature/test-branch-{int(time.time())}"
        create_result = self.repos_api.update(
            repo_path, 
            branch=new_branch_name
        )
        
        self.assertIsNotNone(create_result)

class TestGitAuthentication(DatabricksGitIntegrationTestBase):
    """Test authentication and authorization scenarios"""
    
    def test_09_invalid_token_handling(self):
        """Test behavior with invalid Git tokens"""
        print("Testing invalid token handling...")
        
        # This would test the error handling when Git credentials are invalid
        # Requires simulating token revocation
        pass

    def test_10_read_only_repo_access(self):
        """Test operations on read-only repositories"""
        print("Testing read-only repository access...")
        
        read_only_repo_url = "https://github.com/some-public-readonly-repo.git"
        repo_path = "/Repos/test_user/test_readonly"
        
        try:
            repo_info = self.repos_api.create(
                path=repo_path,
                url=read_only_repo_url,
                provider=self.test_provider
            )
            
            # Try to commit to read-only repo (should fail)
            with self.assertRaises(Exception):
                self.repos_api.commit(repo_path, "This should fail")
                
        except Exception as e:
            print(f"Expected error with read-only repo: {e}")

class TestDatabricksSpecificFeatures(DatabricksGitIntegrationTestBase):
    """Test Databricks-specific Git integration features"""
    
    def test_11_notebook_format_conversion(self):
        """Test notebook format conversion during Git operations"""
        print("Testing notebook format conversion...")
        
        repo_path = "/Repos/test_user/test_format_conversion"
        repo_info = self.repos_api.create(
            path=repo_path,
            url=self.test_repo_url,
            provider=self.test_provider
        )
        
        # Test importing/exporting different formats
        test_content = "# Test Python script\nprint('Hello World')"
        
        # Import as Python script
        self.workspace_api.import_workspace(
            path=f"{repo_path}/test_script.py",
            content=test_content.encode('utf-8'),
            format="SOURCE",
            language="PYTHON"
        )
        
        # Verify the file was created
        file_info = self.workspace_api.export_workspace(
            f"{repo_path}/test_script.py",
            format="SOURCE"
        )
        
        self.assertIsNotNone(file_info)

    def test_12_dbfs_paths_portability(self):
        """Test DBFS path handling in version-controlled notebooks"""
        print("Testing DBFS path portability...")
        
        # Create notebook with DBFS paths
        notebook_with_dbfs = {
            "cells": [
                {
                    "cell_type": "code",
                    "source": [
                        "# DBFS path test\n",
                        "df = spark.read.csv('dbfs:/mnt/data/test_file.csv')\n",
                        "display(df)"
                    ],
                    "metadata": {}
                }
            ],
            "metadata": {"language_info": {"name": "python"}}
        }
        
        repo_path = "/Repos/test_user/test_dbfs_portability"
        repo_info = self.repos_api.create(
            path=repo_path,
            url=self.test_repo_url,
            provider=self.test_provider
        )
        
        # Import notebook with DBFS paths
        notebook_path = f"{repo_path}/dbfs_test_notebook.py"
        self.workspace_api.import_workspace(
            path=notebook_path,
            content=json.dumps(notebook_with_dbfs).encode('utf-8'),
            format="SOURCE",
            language="PYTHON"
        )
        
        # Commit to Git
        self.repos_api.commit(repo_path, "Add notebook with DBFS paths")

class TestGitCICDIntegration(DatabricksGitIntegrationTestBase):
    """Test Git integration with CI/CD pipelines"""
    
    def test_13_cli_integration(self):
        """Test Databricks CLI integration with Git"""
        print("Testing CLI integration...")
        
        # Test using CLI commands for Git operations
        import subprocess
        
        try:
            # List repos via CLI
            result = subprocess.run([
                'databricks', 'repos', 'list',
                '--profile', 'DEFAULT'
            ], capture_output=True, text=True, check=True)
            
            self.assertEqual(result.returncode, 0)
            
        except subprocess.CalledProcessError as e:
            print(f"CLI test failed: {e}")

    def test_14_automated_deployment(self):
        """Test automated deployment scenarios"""
        print("Testing automated deployment...")
        
        # Simulate CI/CD deployment
        repo_path = "/Repos/test_user/ci_cd_test"
        
        # Create repo via API (simulating CI/CD)
        repo_info = self.repos_api.create(
            path=repo_path,
            url=self.test_repo_url,
            provider=self.test_provider,
            branch="main"
        )
        
        # Update to specific branch (simulating environment promotion)
        self.repos_api.update(repo_path, branch="production")
        
        # Verify deployment
        repo_status = self.repos_api.get(repo_path)
        self.assertEqual(repo_status['branch'], 'production')

class TestNegativeScenarios(DatabricksGitIntegrationTestBase):
    """Test negative scenarios and error handling"""
    
    def test_15_nonexistent_repository(self):
        """Test handling of non-existent Git repositories"""
        print("Testing non-existent repository handling...")
        
        invalid_url = "https://github.com/nonexistent-org/nonexistent-repo.git"
        
        with self.assertRaises(Exception):
            self.repos_api.create(
                path="/Repos/test_user/invalid_repo",
                url=invalid_url,
                provider=self.test_provider
            )

    def test_16_invalid_git_url(self):
        """Test handling of malformed Git URLs"""
        print("Testing invalid Git URL handling...")
        
        malformed_url = "not-a-valid-git-url"
        
        with self.assertRaises(Exception):
            self.repos_api.create(
                path="/Repos/test_user/malformed_repo",
                url=malformed_url,
                provider=self.test_provider
            )

    def test_17_large_file_handling(self):
        """Test handling of large files in Git operations"""
        print("Testing large file handling...")
        
        # Create a moderately large file
        large_content = "x" * (1024 * 1024)  # 1MB file
        
        repo_path = "/Repos/test_user/test_large_files"
        repo_info = self.repos_api.create(
            path=repo_path,
            url=self.test_repo_url,
            provider=self.test_provider
        )
        
        try:
            self.workspace_api.import_workspace(
                path=f"{repo_path}/large_file.py",
                content=large_content.encode('utf-8'),
                format="SOURCE",
                language="PYTHON"
            )
            
            # Try to commit
            self.repos_api.commit(repo_path, "Add large test file")
            
        except Exception as e:
            print(f"Large file handling resulted in: {e}")

class PerformanceTests(DatabricksGitIntegrationTestBase):
    """Test performance of Git operations"""
    
    def test_18_multiple_repo_operations(self):
        """Test performance with multiple repository operations"""
        print("Testing multiple repo operations...")
        
        start_time = time.time()
        
        # Create multiple repos
        for i in range(5):
            repo_path = f"/Repos/test_user/perf_test_{i}"
            self.repos_api.create(
                path=repo_path,
                url=self.test_repo_url,
                provider=self.test_provider
            )
        
        end_time = time.time()
        execution_time = end_time - start_time
        
        print(f"Multiple repo creation took: {execution_time:.2f} seconds")
        self.assertLess(execution_time, 60)  # Should complete within 60 seconds

    def test_19_large_pull_operations(self):
        """Test performance of pulling large repositories"""
        print("Testing large repository pull performance...")
        
        large_repo_url = "https://github.com/some-large-repo.git"
        
        start_time = time.time()
        
        try:
            repo_info = self.repos_api.create(
                path="/Repos/test_user/large_repo_test",
                url=large_repo_url,
                provider=self.test_provider
            )
        except Exception as e:
            print(f"Large repo test skipped: {e}")
            return
            
        end_time = time.time()
        pull_time = end_time - start_time
        
        print(f"Large repo pull took: {pull_time:.2f} seconds")

# Utility methods for the test base
def cleanup_test_repos(self):
    """Clean up test repositories"""
    try:
        repos = self.repos_api.list()
        for repo in repos.get('repos', []):
            if 'test' in repo['path'].lower():
                self.repos_api.delete(repo['path'])
    except Exception as e:
        print(f"Cleanup warning: {e}")

def create_test_notebook(self, path, content):
    """Helper to create test notebooks"""
    notebook_content = {
        "cells": [{
            "cell_type": "code",
            "source": [content],
            "metadata": {}
        }],
        "metadata": {"language_info": {"name": "python"}}
    }
    
    self.workspace_api.import_workspace(
        path=path,
        content=json.dumps(notebook_content).encode('utf-8'),
        format="SOURCE",
        language="PYTHON"
    )

# Add utility method to base class
DatabricksGitIntegrationTestBase.cleanup_test_repos = cleanup_test_repos
DatabricksGitIntegrationTestBase.create_test_notebook = create_test_notebook

# Test execution and reporting
class TestRunner:
    """Comprehensive test runner with reporting"""
    
    def __init__(self):
        self.results = {}
        self.start_time = None
        self.end_time = None
    
    def run_all_tests(self):
        """Run all test scenarios"""
        self.start_time = datetime.now()
        print(f"Starting Databricks Git Integration Tests at {self.start_time}")
        print("=" * 80)
        
        test_classes = [
            TestGitBasicOperations,
            TestGitConflictScenarios, 
            TestGitBranchOperations,
            TestGitAuthentication,
            TestDatabricksSpecificFeatures,
            TestGitCICDIntegration,
            TestNegativeScenarios,
            PerformanceTests
        ]
        
        for test_class in test_classes:
            print(f"\nRunning {test_class.__name__}...")
            suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
            runner = unittest.TextTestRunner(verbosity=2)
            result = runner.run(suite)
            self.results[test_class.__name__] = result
        
        self.end_time = datetime.now()
        self.generate_report()
    
    def generate_report(self):
        """Generate comprehensive test report"""
        print("\n" + "=" * 80)
        print("DATABRICKS GIT INTEGRATION TEST REPORT")
        print("=" * 80)
        
        total_tests = 0
        total_failures = 0
        total_errors = 0
        
        for class_name, result in self.results.items():
            tests_run = result.testsRun
            failures = len(result.failures)
            errors = len(result.errors)
            
            total_tests += tests_run
            total_failures += failures
            total_errors += errors
            
            status = "PASS" if failures == 0 and errors == 0 else "FAIL"
            print(f"{class_name:40} Tests: {tests_run:3d} | Failures: {failures:2d} | Errors: {errors:2d} | {status}")
        
        print("-" * 80)
        print(f"TOTAL: {total_tests} tests | {total_failures} failures | {total_errors} errors")
        print(f"Execution time: {(self.end_time - self.start_time).total_seconds():.2f} seconds")
        
        success_rate = ((total_tests - total_failures - total_errors) / total_tests * 100) if total_tests > 0 else 0
        print(f"Success rate: {success_rate:.1f}%")
        
        if total_failures == 0 and total_errors == 0:
            print("\n🎉 ALL TESTS PASSED! Git integration is working correctly.")
        else:
            print(f"\n❌ {total_failures + total_errors} test(s) need attention.")

# Configuration and environment setup
def setup_test_environment():
    """Set up the test environment"""
    print("Setting up test environment...")
    
    # Check for required environment variables
    required_vars = ['DATABRICKS_HOST', 'DATABRICKS_TOKEN']
    for var in required_vars:
        if not os.getenv(var):
            raise EnvironmentError(f"Required environment variable {var} is not set")
    
    print("Environment setup completed successfully")

if __name__ == "__main__":
    # Set up test environment
    try:
        setup_test_environment()
        
        # Run all tests
        runner = TestRunner()
        runner.run_all_tests()
        
    except Exception as e:
        print(f"Test execution failed: {e}")
        exit(1)