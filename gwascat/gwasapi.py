import requests

class Gwasapi:
    def __init__(self):
        pass

    def get_metadata(self):
        """
        Fetch metadata from the GWAS Catalog API.
        Returns the JSON response as a Python dict.
        """
        url = "https://www.ebi.ac.uk/gwas/rest/api/v2/metadata"
        headers = {"accept": "application/json"}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()

    def get_studies(
        self,
        pubmed_id=None,
        disease_trait=None,
        full_pvalue_set=None,
        efo_id=None,
        efo_trait=None,
        accession_id=None,
        cohort=None,
        gxe=None,
        ancestral_group=None,
        no_of_individuals=None,
        show_child_trait=None,
        mapped_gene=None,
        extended_geneset=None,
        sort=None,
        direction=None,
        page=None,
        size=None
    ):
        """
        Fetch studies from the GWAS Catalog API.
        Only parameters with non-None values are sent as query parameters.
        Returns the JSON response as a Python dict.
        """
        url = "https://www.ebi.ac.uk/gwas/rest/api/v2/studies"
        headers = {"accept": "application/json"}
        params = {}
        if pubmed_id is not None:
            params["pubmedId"] = pubmed_id
        if disease_trait is not None:
            params["diseaseTrait"] = disease_trait
        if full_pvalue_set is not None:
            params["fullPvalueSet"] = full_pvalue_set
        if efo_id is not None:
            params["efoId"] = efo_id
        if efo_trait is not None:
            params["efoTrait"] = efo_trait
        if accession_id is not None:
            params["accessionId"] = accession_id
        if cohort is not None:
            params["cohort"] = cohort
        if gxe is not None:
            params["gxe"] = gxe
        if ancestral_group is not None:
            params["ancestralGroup"] = ancestral_group
        if no_of_individuals is not None:
            params["noOfIndividuals"] = no_of_individuals
        if show_child_trait is not None:
            params["showChildTrait"] = show_child_trait
        if mapped_gene is not None:
            params["mappedGene"] = mapped_gene
        if extended_geneset is not None:
            params["extendedGeneset"] = extended_geneset
        if sort is not None:
            params["sort"] = sort
        if direction is not None:
            params["direction"] = direction
        if page is not None:
            params["page"] = page
        if size is not None:
            params["size"] = size

        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()

    def get_study(self, accession_id):
        """
        Fetch a single study from the GWAS Catalog API by accession ID.
        Returns the JSON response as a Python dict.
        Raises HTTPError if not found or on error.
        """
        url = f"https://www.ebi.ac.uk/gwas/rest/api/v2/studies/{accession_id}"
        headers = {"accept": "application/json"}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()

    def get_associations(
        self,
        pubmed_id=None,
        rs_id=None,
        full_pvalue_set=None,
        accession_id=None,
        efo_trait=None,
        efo_id=None,
        show_child_trait=None,
        mapped_gene=None,
        extended_geneset=None,
        sort=None,
        direction=None,
        page=None,
        size=None
    ):
        """
        Fetch associations from the GWAS Catalog API.
        Only parameters with non-None values are sent as query parameters.
        Returns the JSON response as a Python dict.
        """
        url = "https://www.ebi.ac.uk/gwas/rest/api/v2/associations"
        headers = {"accept": "application/json"}
        params = {}
        if pubmed_id is not None:
            params["pubmedId"] = pubmed_id
        if rs_id is not None:
            params["rsId"] = rs_id
        if full_pvalue_set is not None:
            params["fullPvalueSet"] = full_pvalue_set
        if accession_id is not None:
            params["accessionId"] = accession_id
        if efo_trait is not None:
            params["efoTrait"] = efo_trait
        if efo_id is not None:
            params["efoId"] = efo_id
        if show_child_trait is not None:
            params["showChildTrait"] = show_child_trait
        if mapped_gene is not None:
            params["mappedGene"] = mapped_gene
        if extended_geneset is not None:
            params["extendedGeneset"] = extended_geneset
        if sort is not None:
            params["sort"] = sort
        if direction is not None:
            params["direction"] = direction
        if page is not None:
            params["page"] = page
        if size is not None:
            params["size"] = size

        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()

    def get_association(self, association_id):
        """
        Fetch a single association from the GWAS Catalog API by association ID.
        Returns the JSON response as a Python dict.
        Raises HTTPError if not found or on error.
        """
        url = f"https://www.ebi.ac.uk/gwas/rest/api/v2/associations/{association_id}"
        headers = {"accept": "application/json"}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()

    def get_publications(
        self,
        pubmed_id=None,
        title=None,
        first_author=None,
        sort=None,
        direction=None,
        page=None,
        size=None
    ):
        """
        Fetch publications from the GWAS Catalog API.
        Only parameters with non-None values are sent as query parameters.
        Returns the JSON response as a Python dict.
        """
        url = "https://www.ebi.ac.uk/gwas/rest/api/v2/publications"
        headers = {"accept": "application/json"}
        params = {}
        if pubmed_id is not None:
            params["pubmedId"] = pubmed_id
        if title is not None:
            params["title"] = title
        if first_author is not None:
            params["firstAuthor"] = first_author
        if sort is not None:
            params["sort"] = sort
        if direction is not None:
            params["direction"] = direction
        if page is not None:
            params["page"] = page
        if size is not None:
            params["size"] = size

        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()

    def get_publication(self, pubmed_id):
        """
        Fetch a single publication from the GWAS Catalog API by pubmed_id.
        Returns the JSON response as a Python dict.
        Raises HTTPError if not found or on error.
        """
        url = f"https://www.ebi.ac.uk/gwas/rest/api/v2/publications/{pubmed_id}"
        headers = {"accept": "application/json"}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()

    def get_efo_traits(
        self,
        efo_trait=None,
        uri=None,
        efo_id=None,
        pubmed_id=None,
        mapped_gene=None,
        extended_geneset=None,
        sort=None,
        direction=None,
        page=None,
        size=None
    ):
        """
        Fetch EFO traits from the GWAS Catalog API.
        Only parameters with non-None values are sent as query parameters.
        Returns the JSON response as a Python dict.
        """
        url = "https://www.ebi.ac.uk/gwas/rest/api/v2/efo-traits"
        headers = {"accept": "application/json"}
        params = {}
        if efo_trait is not None:
            params["efoTrait"] = efo_trait
        if uri is not None:
            params["uri"] = uri
        if efo_id is not None:
            params["efoId"] = efo_id
        if pubmed_id is not None:
            params["pubmedId"] = pubmed_id
        if mapped_gene is not None:
            params["mappedGene"] = mapped_gene
        if extended_geneset is not None:
            params["extendedGeneset"] = extended_geneset
        if sort is not None:
            params["sort"] = sort
        if direction is not None:
            params["direction"] = direction
        if page is not None:
            params["page"] = page
        if size is not None:
            params["size"] = size

        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()

    def get_efo_trait(self, efo_id):
        """
        Fetch a single EFO trait from the GWAS Catalog API by efo_id.
        Returns the JSON response as a Python dict.
        Raises HTTPError if not found or on error.
        """
        url = f"https://www.ebi.ac.uk/gwas/rest/api/v2/efo-traits/{efo_id}"
        headers = {"accept": "application/json"}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()

    def get_snps(
        self,
        rs_id=None,
        bp_location=None,
        bp_start=None,
        bp_end=None,
        pubmed_id=None,
        chromosome=None,
        mapped_gene=None,
        extended_geneset=None,
        sort=None,
        direction=None,
        page=None,
        size=None
    ):
        """
        Fetch SNPs from the GWAS Catalog API.
        Only parameters with non-None values are sent as query parameters.
        Returns the JSON response as a Python dict.
        """
        url = "https://www.ebi.ac.uk/gwas/rest/api/v2/single-nucleotide-polymorphisms"
        headers = {"accept": "application/json"}
        params = {}
        if rs_id is not None:
            params["rsId"] = rs_id
        if bp_location is not None:
            params["bpLocation"] = bp_location
        if bp_start is not None:
            params["bpStart"] = bp_start
        if bp_end is not None:
            params["bpEnd"] = bp_end
        if pubmed_id is not None:
            params["pubmedId"] = pubmed_id
        if chromosome is not None:
            params["chromosome"] = chromosome
        if mapped_gene is not None:
            params["mappedGene"] = mapped_gene
        if extended_geneset is not None:
            params["extendedGeneset"] = extended_geneset
        if sort is not None:
            params["sort"] = sort
        if direction is not None:
            params["direction"] = direction
        if page is not None:
            params["page"] = page
        if size is not None:
            params["size"] = size

        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()

    def get_snp(self, rs_id):
        """
        Fetch a single SNP from the GWAS Catalog API by rs_id.
        Returns the JSON response as a Python dict.
        Raises HTTPError if not found or on error.
        """
        url = f"https://www.ebi.ac.uk/gwas/rest/api/v2/single-nucleotide-polymorphisms/{rs_id}"
        headers = {"accept": "application/json"}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()

    def get_genomic_contexts(
        self,
        rs_id,
        sort=None,
        direction=None
    ):
        """
        Fetch all genomic contexts for a SNP from the GWAS Catalog API.
        Returns the JSON response as a Python dict.
        """
        url = f"https://www.ebi.ac.uk/gwas/rest/api/v2/single-nucleotide-polymorphisms/{rs_id}/genomic-contexts"
        headers = {"accept": "application/json"}
        params = {}
        if sort is not None:
            params["sort"] = sort
        if direction is not None:
            params["direction"] = direction

        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()

    def get_genomic_context(self, rs_id, genomic_context_id):
        """
        Fetch a single genomic context for a SNP from the GWAS Catalog API by rs_id and genomicContext_id.
        Returns the JSON response as a Python dict.
        Raises HTTPError if not found or on error.
        """
        url = f"https://www.ebi.ac.uk/gwas/rest/api/v2/single-nucleotide-polymorphisms/{rs_id}/genomic-contexts/{genomic_context_id}"
        headers = {"accept": "application/json"}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()

    def get_genes(
        self,
        page=None,
        size=None,
        sort=None
    ):
        """
        Fetch genes from the GWAS Catalog API.
        Only parameters with non-None values are sent as query parameters.
        Returns the JSON response as a Python dict.
        """
        url = "https://www.ebi.ac.uk/gwas/rest/api/v2/genes"
        headers = {"accept": "application/json"}
        params = {}
        if page is not None:
            params["page"] = page
        if size is not None:
            params["size"] = size
        if sort is not None:
            params["sort"] = sort

        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()

    def get_gene(self, gene_name):
        """
        Fetch a single gene from the GWAS Catalog API by gene_name.
        Returns the JSON response as a Python dict.
        Raises HTTPError if not found or on error.
        """
        url = f"https://www.ebi.ac.uk/gwas/rest/api/v2/genes/{gene_name}"
        headers = {"accept": "application/json"}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()

    def get_loci(self, association_id):
        """
        Fetch all loci for an association from the GWAS Catalog API.
        Returns the JSON response as a Python dict.
        """
        url = f"https://www.ebi.ac.uk/gwas/rest/api/v2/associations/{association_id}/loci"
        headers = {"accept": "application/json"}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()

    def get_locus(self, association_id, locus_id):
        """
        Fetch a single locus for an association from the GWAS Catalog API.
        Returns the JSON response as a Python dict.
        """
        url = f"https://www.ebi.ac.uk/gwas/rest/api/v2/associations/{association_id}/loci/{locus_id}"
        headers = {"accept": "application/json"}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()

    def get_body_of_works(
        self,
        title=None,
        first_author=None,
        page=None,
        size=None,
        sort=None
    ):
        """
        Fetch all body of works from the GWAS Catalog API.
        Only parameters with non-None values are sent as query parameters.
        Returns the JSON response as a Python dict.
        """
        url = "https://www.ebi.ac.uk/gwas/rest/api/v2/body-of-works"
        headers = {"accept": "application/json"}
        params = {}
        if title is not None:
            params["title"] = title
        if first_author is not None:
            params["firstAuthor"] = first_author
        if page is not None:
            params["page"] = page
        if size is not None:
            params["size"] = size
        if sort is not None:
            params["sort"] = sort

        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()

    def get_body_of_work(self, bow_id):
        """
        Fetch a single body of work from the GWAS Catalog API by bow_id.
        Returns the JSON response as a Python dict.
        """
        url = f"https://www.ebi.ac.uk/gwas/rest/api/v2/body-of-works/{bow_id}"
        headers = {"accept": "application/json"}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()

    def get_unpublished_studies_for_body_of_work(
        self,
        bow_id,
        page=None,
        size=None,
        sort=None
    ):
        """
        Fetch all unpublished studies for a body of work from the GWAS Catalog API.
        Only parameters with non-None values are sent as query parameters.
        Returns the JSON response as a Python dict.
        """
        url = f"https://www.ebi.ac.uk/gwas/rest/api/v2/body-of-works/{bow_id}/unpublished-studies"
        headers = {"accept": "application/json"}
        params = {}
        if page is not None:
            params["page"] = page
        if size is not None:
            params["size"] = size
        if sort is not None:
            params["sort"] = sort

        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()

    def get_unpublished_studies(
        self,
        disease_trait=None,
        accession_id=None,
        title=None,
        first_author=None,
        cohort=None,
        sort=None,
        direction=None,
        page=None,
        size=None
    ):
        """
        Fetch all unpublished studies from the GWAS Catalog API.
        Only parameters with non-None values are sent as query parameters.
        Returns the JSON response as a Python dict.
        """
        url = "https://www.ebi.ac.uk/gwas/rest/api/v2/unpublished-studies"
        headers = {"accept": "application/json"}
        params = {}
        if disease_trait is not None:
            params["diseaseTrait"] = disease_trait
        if accession_id is not None:
            params["accessionId"] = accession_id
        if title is not None:
            params["title"] = title
        if first_author is not None:
            params["firstAuthor"] = first_author
        if cohort is not None:
            params["cohort"] = cohort
        if sort is not None:
            params["sort"] = sort
        if direction is not None:
            params["direction"] = direction
        if page is not None:
            params["page"] = page
        if size is not None:
            params["size"] = size

        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()

    def get_unpublished_study(self, accession_id):
        """
        Fetch a single unpublished study from the GWAS Catalog API by accession_id.
        Returns the JSON response as a Python dict.
        """
        url = f"https://www.ebi.ac.uk/gwas/rest/api/v2/unpublished-studies/{accession_id}"
        headers = {"accept": "application/json"}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()

    def get_unpublished_ancestries(
        self,
        accession_id,
        sort=None,
        direction=None
    ):
        """
        Fetch all unpublished ancestries for an unpublished study from the GWAS Catalog API.
        Returns the JSON response as a Python dict.
        """
        url = f"https://www.ebi.ac.uk/gwas/rest/api/v2/unpublished-studies/{accession_id}/unpublished-ancestries"
        headers = {"accept": "application/json"}
        params = {}
        if sort is not None:
            params["sort"] = sort
        if direction is not None:
            params["direction"] = direction

        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()

    def get_unpublished_ancestry(self, accession_id, ancestry_id):
        """
        Fetch a single unpublished ancestry for an unpublished study from the GWAS Catalog API.
        Returns the JSON response as a Python dict.
        """
        url = f"https://www.ebi.ac.uk/gwas/rest/api/v2/unpublished-studies/{accession_id}/unpublished-ancestries/{ancestry_id}"
        headers = {"accept": "application/json"}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()


