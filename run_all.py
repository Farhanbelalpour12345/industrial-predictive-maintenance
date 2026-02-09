import subprocess
import sys

def run_step(description, module_name):
    print(f"\n🚀 {description} ...")
    
    result = subprocess.run(
        [sys.executable, "-m", module_name],
        capture_output=True,
        text=True
    )

    print(result.stdout)

    if result.returncode != 0:
        print("❌ Error occurred:")
        print(result.stderr)
        sys.exit(1)

    print(f"✅ {description} completed.")


if __name__ == "__main__":
    run_step("Running data processing pipeline",
             "src.processing.run_full_pipeline")

    run_step("Training RUL model",
             "src.models.rul_regression")

    run_step("Saving processed data to PostgreSQL",
             "src.database.save_processed_data")

    run_step("Saving predictions to PostgreSQL",
             "src.database.save_predictions")

    print("\n🎉 FULL PIPELINE EXECUTED SUCCESSFULLY")
