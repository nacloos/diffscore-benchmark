from pathlib import Path
from functools import partial

from diffscore import Measure, Card
from diffscore.analysis import pipeline_optim_score, decoder_logistic


if __name__ == "__main__":
    datasets = [
        # "ultrametric",
        # "MajajHong2015",
        # "FreemanZiemba2013",
        # "Hatsopoulos2007",
        "Mante2013",
        # "siegel15-FEF-stim_period-var99"
    ]
    measures = [
        "cka",
        # "cka-angular-score",
        # "nbs",
        # "procrustes-angular-score",
        # "linreg",
        # "rsa-correlation-corr",
        # "ridge-lambda100-r2#5folds_cv",
        # "linreg"
    ]
    # all the scoring measures
    # measures = [
    #     measure_id.split(".")[-1] for measure_id in Measure("*").keys() if "score" in Card(measure_id.split(".")[-1])["props"]
    # ]
    # TODO: cca-angular-score MajajHong NaN grad
    print(measures)

    # save score by measure and aggregate everything in another function
    for dataset in datasets:
        _save_dir = Path(__file__).parent / "data" / "benchmarks_cka" / dataset
        pipeline_optim_score(
            dataset=dataset,
            measure=measures,
            stop_score=0.99,
            decoder="logistic",
            save_dir=_save_dir,
        )

        # res = diffscore.optimize(dataset=dataset, measure=measure, stop_score=0.99)
        # diffscore.analyze(res, decoder="logistic", save_dir=_save_dir)
