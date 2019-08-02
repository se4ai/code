## Quiz2: SI and AI


Find papers in the recent SE literature that use:

- TERMS=  "software engineering and data mining"
- TERMS=  "software engineering and optimization"
- TERMS=  "software engineering and prover"


Method1: see if you can find your term in  [this paper](https://arxiv.org/pdf/1812.01550.pdf). If so, use references from this 
papers.

Method2:

- For TERM in TERMS, go to Google Scholar Advanced Search
    - For VENUE in one of {ICSE, FSE, ASE, "transactions software engineering", "Empirical Software Engineering", "Journal of Systems and Software", "Information Software Technologies"} do
         - Set "Return articles published in" to VENUE
         - Set "with all at least one the words" to TERM 
         - Set "with the exact phrase" set to "software engineering" to TERM 
         - Set "Return articles dated between" to the last ten years
         - Find a  paper that uses TERM in an interesting way. 
           Hint: only read paper with "enough" citations citations (for the last two years, "enough"=0; for anything
           before that, then "enough" for data mining =12 cites/year, "enough" for optimization is 6 cites/year, and for prover, 10 cites ever )
         - Sumamrize the paper under the following headings (usually, 2-3 lines each).

![](/img/googlesearch.png)

Note that most of the time for this exercise will be spent
reading N dull papers before you find one you can read, and that your like.

Headings:

- Your name():
- Term:
- Write a ten line summary of what this does? Input? Output? Processing? Indications for when to use it? Not use it?
- Paper Title:
- Year:
- Venue:
- Authors:
- URL for download (if you can find it):
- Requirements (if found): what was the goal of the work? anything declared out of scope?
- Data collection (if mentioned): how was it done?
- Data cleaning (if done): any sanity checks on the data? repairs to strange fields?
- Data labelling (if needed): any need to assign values to the data before anything else (e.g. "good project", "this is a bad poject"). How was it done? How were those labels checked? What was the effort in that labelling process?
- Training (if done): how was it done? Anything mentioned about issues with training? (e.g. long CPU times)
- Evaluation (if done): what metrics were applied (define each one)? how were the results summarized (list statistical tests and visualizations used). If cool visualizations, include them here.
- Deployment (if done): how was this scaled up? Delivered to many users?
- Monitoring (if done): if deployed, how did the developers watch over this development?
