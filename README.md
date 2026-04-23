# Field Estimate Tool

## The Problem

Our HVAC technicians are losing time on every service call.

Right now, when a tech gets to a job site and needs to give the customer an estimate, here's what happens: they flip through a product binder or scroll through a spreadsheet on their phone, look up equipment costs, try to remember the labor rates for different job types, factor in the specifics of the property, and then scribble numbers on a notepad or punch them into a calculator. Sometimes they call the office to double-check pricing. Sometimes they guess and adjust later.

The customer is standing there the whole time.

A simple repair estimate might take 10-15 minutes. A full system replacement quote can take 30-45 minutes on-site, and that's before the tech has to go back to their truck to write it up in a way the customer can actually read. Some techs text a photo of their handwritten notes to the office and have someone there type it up. Others just wing it and send a "real" estimate later that evening.

We've got about 40 technicians in the field. If each one does 4-6 estimates a day, that's a lot of wasted time — and a lot of customers standing around waiting. We've heard from customers that the wait makes the whole experience feel less professional, and we've definitely lost jobs because a competitor got a clean estimate out faster.

## What We Have

In the `data/` folder, you'll find some of the information our techs work with:

- **equipment.json** — Our catalog of HVAC equipment and parts with pricing
- **labor_rates.json** — What we charge for different types of work
- **customers.json** — A sample of customer and property records

This is real-ish data pulled from our systems. It's not perfect — some of it was exported from different tools at different times, so it might not all look the same.

## What We're Asking

Build something that helps.

Fork this repo, build your solution, and include a short write-up explaining your approach — what you built, why you made the choices you did, and what you'd do differently with more time.

## My approach

I approached this project with a strong focus on the intended users, which are the HVAC technicians. From the original problem, I identified that the main problem was minimizing the time and effort required to look up information and generate estimates. I thought that since technicians typically already understand the problem they are dealing with; they mainly just need a fast way to translate that knowledge into a price estimate. Based on that, I designed a system that allows the technician to quickly select the job type, level, and required equipment, and then automatically generates a price range.

The application first collects basic customer information, such as name and property type (required), along with optional details like square footage and system type. It then prompts the technician to select the job type and complexity level, followed by the relevant equipment. Using this information, the system calculates and displays a final price range based on equipment costs and labor estimates.

I chose to implement the project as a lightweight web application using Flask and all you have to do is run python app.py to see the program. I considered more advanced approaches, such as allowing technicians to input free-form text and using natural language processing to interpret the job, or building a dynamic decision tree that suggests equipment in real time. However, I ultimately chose a more straightforward design because it is faster to implement and aligns with how technicians are currently generating quotes, minimizing the learning curve.

If I had more time, I would expand the application with additional features. For example, I would implement persistent storage to save and display past quotes, as well as allow users to edit and reuse them. I would also improve the organization and searchability of equipment to make selection even faster. Finally, I think I would implement a more dynamic interface as mentioned above, that updates the total cost in real time as the user makes selections. This makes it easier for technicians to quickly compare options without navigating backward through the workflow.

Overall I did have fun coming up with a solution for this problem and I really appreciate this opportunity provided!