import scrapy
from datetime import datetime
from scrapy.linkextractors import LinkExtractor


class IndeedSpider(scrapy.Spider):
    name = 'indeed'
    allowed_domains = ['www.indeed.com/']
    start_urls = ['https://www.indeed.com/jobs?q=react&l=Remote']
    # today = []

    def parse(self, response):
        #extraemos el contenedor pricipal
        link_cont_elemts  = response.xpath('(//td/div[4]/div[1]/a)')

        for lc_elemts in link_cont_elemts:
            link            = lc_elemts.xpath('.//@href').get()
            today           = datetime.today().strftime('%Y-%m-%d')
            title_elem      = lc_elemts.xpath('.//h2/span/text()').get()
            location_elem   = lc_elemts.xpath('.//table[1]/tbody/tr/td/div[2]/pre/div/text()').get()
            company_elem    = lc_elemts.xpath('.//td/div[2]/pre/span/text()').get()
            apply_to        = lc_elemts.xpath('.//table[1]/tbody/tr/td/div[3]/div/span/text()').get()
            salary_tag      = lc_elemts.xpath('.//table[1]/tbody/tr/td/div[3]/div/span/text()').get()
            post_date       = lc_elemts.xpath('.//table[2]/tbody/tr[2]/td/div[1]/span[1]/text()').get()
            sumary          = lc_elemts.xpath('.//table[2]/tbody/tr[2]/td/div[1]/div/ul/li/text()').get()

            if salary_tag:
                salary      = salary_tag
            else:
                salary      = ''  

            # # Absolute URL
            absolute_url = response.urljoin(link)
    

            yield {
                'link': absolute_url,
                'today': today,
                'sumary': sumary,
                'salary': salary,
                'apply_to': apply_to,
                'post_date': post_date,
                'title_elem': title_elem,               
                'company_elem': company_elem, 
                'location_elem': location_elem,
            }

    # Relative link
            # yield response.follow(url=link, callback=self.parse_applyto)

    
    def parse_applyto(self, response):
        # Data extracted from the main page
        # extract_date = response.request.meta['extract_date']
        # location = response.request.meta['location']
        # company_name = response.request.meta['company_name']
        # post_date = response.request.meta['post_date']
        # job_description = response.request.meta['job_description']
        # salary = response.request.meta['salary']

        # Data extracted from the link apply to company, to obtain the link apply to
        job_title = response.xpath('//h1/text()').get()
        apply_to = response.xpath('(//div/div[2]/a)[6]/@href').get()

        yield {
            # 'Extract_date': extract_date,
            # 'Location': location,
            # 'Company_name': company_name,
            # 'Post_date': post_date,
            # 'Job_description': job_description,
            # 'Salary': salary,
            'job_title': job_title,               
            'Apply_to': apply_to,
        }


