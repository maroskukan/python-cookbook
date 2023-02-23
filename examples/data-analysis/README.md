# Python for Data Analysts

Course notes from [Python for Data Analysts](https://app.pluralsight.com/library/courses/python-data-analysts/table-of-contents) by [Janani Ravi](https://app.pluralsight.com/profile/author/janani-ravi).


## Environment

I recommend creating a new python virtual environment for this project using pyenv.

```bash
pyenv virtualenv 3.11.1 data-analysis
pip install --upgrade pip setuptools
pip install -r requirements.txt
```


## Interconnected calculations

### Processing

There are two types of data processing:

Transactional Processing
- Ensures correctness of individual entries
- Access to recent data, from the last few hours or days
- Updates data
- Fast real-time access
- Usually a single data source

Analytical Processing:
- Analyzes large batches of data
- Access to older data going back months or even years
- Mostly reads data
- Long running jobs
- Multiple data sources

