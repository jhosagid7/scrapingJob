            # Absolute link
            # absolute_url = response.urljoin(link) PostDate,Summary,Salary,JobUrl

            # Relative link
    #         yield response.follow(url=link, callback=self.parse_applyto, meta={'extract_date':extract_date,'location':location,'company_name':company_name,'post_date':post_date,'job_description':job_description,'salary':salary})

    
    # def parse_applyto(self, response):
    #     # Data extracted from the main page
    #     extract_date = response.request.meta['extract_date']
    #     location = response.request.meta['location']
    #     company_name = response.request.meta['company_name']
    #     post_date = response.request.meta['post_date']
    #     job_description = response.request.meta['job_description']
    #     salary = response.request.meta['salary']

    #     # Data extracted from the link apply to company, to obtain the link apply to
    #     job_title = response.xpath('//h1/text()').get()
    #     apply_to = response.xpath('(//div/div[2]/a)[6]/@href').get()

    #     yield {
    #         'Extract_date': extract_date,
    #         'Location': location,
    #         'Company_name': company_name,
    #         'Post_date': post_date,
    #         'Job_description': job_description,
    #         'Salary': salary,
    #         'job_title': job_title,               
    #         'Apply_to': apply_to,
    #     }