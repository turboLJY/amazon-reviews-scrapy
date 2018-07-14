# Automated Framework for Amazon Customer Reviews
Extraction of Amazon Customer Reviews based on a key phrase from a specific or all
Amazon Websites in a fully automated manner.

**Disclaimer**: Use only for Research Purposes.

## Description
A Python-based Framework, developed on Windows, which primarily uses the *Scrapy* [[1]](https://doc.scrapy.org/en/latest/) library to create spiders which crawl websites to extract information.

The Customer Reviews extracted include the following metadata:
* ASIN
* Review ID
* Created Date
* Review Title
* Review Author
* Review
* Rating (Stars)
* Helpful Count
* Product Description
* Website
* Country
* Region

### Approach
The Framework uses 2 Spiders to:

1. Fetch ASIN values of all products related to the key phrase.
2. Extract Reviews of all fetched ASIN values.

The User has the choice of either selecting a single country of choice or all countries
in the available database called `AmazonSources`. This is a user-defined class
containing the regions and links of all countries where Amazon has a local website.

**AmazonSources** has the following countries:

Country|
-------|
India |
Japan |
France |
Germany |
Italy |
Netherlands |
Spain |
UK |
Canada |
Mexico |
US |
Australia |
Brazil |
China |

When customer reviews from Non-English websites is extracted, it is instantly converted to the English language with the help of *GoogleTrans* [[2]](http://py-googletrans.readthedocs.io/en/latest/), which uses the **Google Translate Ajax API** to translate for free.
All the customer reviews are finally stored in an `.xlsx` file for further use.

Any Scrapy project can be initialized as:
```
scrapy startproject <project_name>
```

To avoid a website to block any spider created in the Scrapy project,
* Open *settings.py*
* Uncomment *USER_AGENT* and make the following changes:
```python
USER_AGENT = 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.10 (KHTML, like Gecko) Chrome/7.0.540.0 Safari/534.10'
```

To run the framework on other platforms like Linux or MacOS, use a different User Agent which can be copied from [this link](https://developers.whatismybrowser.com/useragents/explore/software_name/chrome/).

### Applications
The result of this framework can be later used for developing various Machine Learning Models for:

* Sentiment Analysis,
* Text Analysis to understand the customer feedbacks, and so on.

## Framework Requirements
* Python 3.6.4

### Package Dependencies
* scrapy
* plac
* pyfiglet
* tqdm
* pandas
* googletrans

## Basic Usage
1. Install Python. As I have used Python *3.6.4*, it is preferred over other versions of Python.
2. Install all package dependencies:
  * Open Terminal as Administrator
  * Use pip to install packages:
  ```
  pip install -U <package_name>
  ```
3. As the framework is automated, only one time execution is required. For only one country:
  ```
  python run_amazon_reviews.py -c <country> -k <key+phrase>
  ```
  For all countries:
  ```
  python run_amazon_reviews.py -c all -k <key+phrase>
  ```
  Use `--help` to get a MAN page of the run_amazon_reviews.py

## License
MIT. See the LICENSE file for the copyright notice.

## Useful Links
[[1]](https://doc.scrapy.org/en/latest/) Scrapy Documentation

[[2]](http://py-googletrans.readthedocs.io/en/latest/) GoogleTrans Documentation
