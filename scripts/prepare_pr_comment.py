import sys

def prepare_failure_commet(repository, issue_number, vendor_label, chart_name):
    msg = f"Thank you for the PR #{issue_number}!\n\n"
    msg += f"There are [some errors](https://github.com/{repository}/pull/{issue_number}/checks) while building and validating your PR. Please check the log for more details.\n\n"
    msg += f'/metadata {{"vendor_label": "{vendor_label}", "chart_name": "{chart_name}"}}\n\n'
    msg += f"Partner Support URL: https://redhat-connect.gitbook.io/red-hat-partner-connect-general-guide/managing-your-account/getting-help/technology-partner-success-desk\n"
    return msg

def prepare_success_commet(issue_number, vendor_label, chart_name):
    msg = f"Thank you for the PR #{issue_number}!\n\n"
    msg += f'/metadata {{"vendor_label": "{vendor_label}", "chart_name": "{chart_name}"}}\n\n'
    return msg

def main():
    result = sys.argv[1]
    repository = sys.argv[2]
    issue_number = open("./pr/NR").read().strip()
    vendor_label = open("./pr/vendor").read().strip()
    chart_name = open("./pr/chart").read().strip()
    if result == "failure":
        msg = prepare_failure_commet(repository, issue_number, vendor_label, chart_name)
    else:
        msg = prepare_success_commet(issue_number, vendor_label, chart_name)

    with open("./pr/comment", "w") as fd:
        fd.write(msg)

if __name__ == "__main__":
    main()