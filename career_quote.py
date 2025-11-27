def enter_job():
    job = input("What is your job?: ")
    return job



def eng_dev_ana(job):
    if job == "ENGINEER":
        job_name = "The engineer has been, and is, a maker of history."
    elif job == "DEVELOPER":
        job_name = "Logical thinking, passion and perseverance is the paint on your palette."
    elif job == "ANALYST":
        job_name = "Seeing what other people can't see gives you great vision."
    else:
        job_name = "I'm sorry. We could not find a quote for your job."
    return job_name



def main():
    job = enter_job()
    job = job.upper()
    print(job)
    job_name = eng_dev_ana(job)
    print(job_name)



main()