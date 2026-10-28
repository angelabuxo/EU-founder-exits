# Final project context · DTU 02805

Summary of the official Week 8 page, “Putting it all together,” and the attached PDF. Source: [Week 8](https://sunelehmann.com/socialgraphs2026-web/weeks/week8.html). Document consulted on 28 October 2026.

## Purpose

The final project is the course exam (50% of the grade). It runs during weeks 9–13 and uses a dataset chosen by the group. The priority is to decide which question is worth answering, find data that can answer it, choose an appropriate measure, and check what that measure captures. An agent can produce many analyses; the important skill is selecting one question and communicating the evidence clearly. The project should center on network science and NLP tools from the course, though other methods may be added where useful.

## Deliverables and schedule

- **Scientific paper:** the PNAS Overleaf template, written in LaTeX, at most six pages including figures and references. Sections: Abstract, Significance Statement, Introduction, Results, Discussion, Methods, and References; include a specific author-contributions statement.
- **Presentation:** three slides, three minutes, followed by questions. Submit the slides as a three-page PDF with the paper. The slides will be combined into one PDF for the session; no laptops need to be connected.
- **Reflection:** at most half a page, ungraded. Say whether the “From an AI-drafted report” boxes on the weekly pages changed how you read your own draft, and where you used them (or did not).
- **Submission deadline:** Friday 27 November 2026, 23:59, on DTU Learn. Submit three PDFs: paper, slides, and reflection.
- **Presentations:** Wednesday 2 December 2026.
- **Project sessions:** 4 November (dataset locked and question drafted), then 11, 18, and 25 November. Groups can be changed until 4 November by updating the registration on Learn.

## Assessment

The paper and presentation receive one combined score on the 0–3 scale. Each reader scores the categories with comments; the teaching team agrees on one grade after the presentations.

1. **Research question:** Is there one? Is it interesting and specific enough to answer?
2. **Data and scope:** Does the dataset contain both a network and text, fit the question, and involve ambitious collection, combination, or perspective?
3. **Use of the course:** Are network science and NLP tools applied, and does the group understand the methods?
4. **Analysis and checks:** Are measurements validated with a null model, a second method, or a hand-labelled sample? Are the results reported, and is it clear what the measurements capture?
5. **Figures:** Do they serve the story, have labelled axes, and captions that tell the reader what to notice?
6. **References:** Are they real, relevant, correct, and do they place the contribution in the literature?
7. **Overall story:** Is the abstract and introduction strong, the writing readable, and the work rigorous and thorough?
8. **Presentation and questions:** Can the group present and defend the work technically?

The presentation checks that the group understands what it submitted. Every member should be able to explain the pipeline, decisions, methods, and why the numbers are reliable.

## Choosing data

The page’s dataset test is:

- both parts are present: **links and text**;
- the suggested scale is hundreds to a few thousand nodes (around 50 is probably too small unless the text or time dimension is unusually rich);
- the data can be obtained in a day;
- the group cares about the domain;
- there is something unknown to investigate.

Combine datasets when that adds value. Data may come from documented or undocumented APIs. When collecting it, respect rate limits, add pauses, and save the working request and a record of what was collected and when. Suggested sources include Wikipedia and Fandom wikis, Bluesky, Reddit, song lyrics and credits, parliamentary speeches, OpenAlex, GitHub, podcasts and guests, TV series and character wikis, recipes, and web endpoints that populate lists. A group member’s hobby can be a good starting point for finding an interesting source.

## Questions, measures, and validation

- The question comes before the method. “We ran X” describes a technique, not a question; state what you want to know and what would count as an answer.
- Iterate: try a question, discover what does not fit, and refine it until the data and question align. The final account can be a clean, coherent story built around the final question.
- Explain what each measure captures and what it does not. For example, modularity measures how grouped a network is, not whether the groups are correct; a sentiment score reflects how a lexicon or classifier behaves on that text; embedding similarity reflects shared context in the training data.
- Validate with a null model (such as a permutation), a second method or comparison (such as NMI or agreement), or a hand-labelled sample (precision, κ). If a model produces a result, also measure its performance on examples you read.
- Compare against the simplest alternative explanation and identify a limitation yourself. A negative result is acceptable if the check supporting it is convincing.
- A text measure can be attached to nodes as an attribute and tested with a permutation. A second network can be built from entities extracted from text and linked by co-occurrence, then validated by reading a sample of its edges.

## Paper and figures

The page recommends two or three decisive figures: three good ones are better than eight. Each figure should answer the question or set up its answer, and show the relevant comparison (null, baseline, or agreement with labels). A large network plot is not a result by itself. The caption should say what is plotted, what comparison is made, and what to notice.

- **Abstract:** 150 words, written last. Include the question, data, main numerical result, and its meaning.
- **Significance Statement:** two or three sentences explaining why the result matters to someone outside the field.
- **Introduction:** question, motivation, what was already known, a one-sentence preview of the answer, and citations to prior work.
- **Results:** tell the story through figures; each figure answers part of the question.
- **Discussion:** explain what the result means and does not mean, and a limitation identified by the group.
- **Methods:** enough detail to reproduce the work: what the data are, their source, collection date and size; preprocessing choices that could change numbers; measures and what they capture; validation and its results.
- **References:** relevant academic sources.
- **Author contributions:** specify who collected the data, built each analysis, labelled examples, and wrote each part. “All group members contributed equally” is not specific enough.

## Presentation and brainstorming session

Suggested structure for the three slides: (1) question and data, (2) main figure, (3) meaning and checks. During the brainstorming session, the group should generate many options, investigate the three most promising (touch the data, estimate its size, and check its source/API), then choose one. The final proposal slide should include:

- the question in one sentence;
- one line describing the data: nodes, links, text, size, and source;
- the measure that answers the question and the course tools it uses;
- the check and the result that would make the group abandon the question;
- a sketch of the planned figure.

Keep the two discarded ideas as well: they can serve as alternatives if the chosen dataset has gaps or the expected effect does not appear.

## Undocumented APIs workshop

Workshop resource: [Inspect Element — Finding Undocumented APIs](https://inspectelement.org/apis.html). In brief: open the browser developer tools → Network → Fetch/XHR; inspect a response and compare it with what the page displays; copy the request as cURL; convert it to Python requests; remove unnecessary headers and parameters; wrap it in a function and loop with pauses; save the requests and collected data. These APIs can provide a scalable way to build datasets, but websites can change, so document the collection method.

## Source

Official page: https://sunelehmann.com/socialgraphs2026-web/weeks/week8.html. The attached PDF is an 18-page printout of the same page, generated on 28 October 2026.
