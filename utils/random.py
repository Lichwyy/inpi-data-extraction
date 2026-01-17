def print_obj(obj):
    print("main",obj.publication_number,"\n",
            obj.application_number,"\n",
            obj.filing_date,"\n",
            obj.publication_date,"\n",
            obj.examination_publication_date,"\n",
            obj.title,"\n",
            obj.abstract,"\n",
            obj.country,"\n",
            obj.source,"\n",
            obj.national_phase_start_date,"\n",
            # obj.priorities[0].number,obj.priorities[0].date,obj.priorities[0].country,"\n",
            # obj.classifications[0].code,obj.classifications[0].year,obj.classifications[0].description,"\n",
            # obj.international_applications[0].application_type,obj.international_applications[0].number,obj.international_applications[0].date,obj.international_applications[0].authority
    )
    print_ot(obj.parties)
def print_ot(list):
    for party in list:
        print(party.name,party.role,party.country)
