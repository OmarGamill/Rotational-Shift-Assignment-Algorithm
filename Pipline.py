import pandas as pd

from ProsessData import load_data, transfrom_data, sort_dataset, process_and_export_schedule
from Utilis import get_experience_shift_counts, print_data as pr_data
from Utilis import increase_total_shifts, schedule_alg_run, calculate_numEmp_req_experience_shift

from writeHere import days, Shifts, table, Path_to_dataset, save_path


def pipline(path_to_dataset=Path_to_dataset, save_path=save_path, print_data=True, save_data=True):

    dataset = load_data(path_to_dataset)

    dataset = transfrom_data(dataset=dataset)
    experience_counts = get_experience_shift_counts(dataset)
    num_of_employees_per_shift_experience = calculate_numEmp_req_experience_shift(
        dataset, exp_level=5)

    for num_day, day in enumerate(days):
        increase_total_shifts(dataset, 0, dataset.shape[0] - 1)  # type: ignore
        schedule_alg_run(
            dataset, Shifts, num_of_employees_per_shift_experience, experience_counts, day, table)
        dataset = sort_dataset(dataset)

    if print_data:
        pr_data(table)

    output_table = process_and_export_schedule(table, save_path, save_data)
