
# Communication Contract with partner
1. Communication will primarily occur via Discord messages. 
2. When one of us posts a question, the other team member should respond within 24 hours. 
3. Feedback should be constructive and respectful.
4. We'll use a version control system (like Git) and regularly push our code, ensuring both team members can access the most recent version of code.
5. Other important documents such as this will be shared via the Canvas Discussion Group page.
6. Since most assignments are due Monday at midnight, it would be a good idea to have a plan developed for group assignments by the preceding Tuesday at midnight. This allows us to anticipate any task dependencies the other team member must complete.

# Instructions for requesting data from the implemented microservice for partner's project
- the microservice implemented in bpmFilter.py will be run in parallel with the program requesting data from it.
- the program requesting data from the microservice will write two integers separated by a whitespace onto request_pipeline.txt
- Example call: request_pipeline.txt << 120 << " " << 130; 

# Instructions for receiving data from the implemented microservice for partner's project
- the microservice will return to response_pipeline a set of row numbers identifying the rows of songs which are included in the bpm range 
- Example return: 
- 2
- 53
- 92

# UML Diagram for view CalendarSummary.py microservice for my project:
     ┌────┐                                ┌────┐                     ┌────────────┐                                
     │User│                                │Main│                     │Microservice│                                
     └─┬──┘                                └─┬──┘                     └─────┬──────┘                                
       │      Input Start and end dates      │                              │                                       
       │ ────────────────────────────────────>                              │                                       
       │                                     │                              │                                       
       │                                     │ Call with start and end dates│                                       
       │                                     │ ─────────────────────────────>                                       
       │                                     │                              │                                       
       │                                     │                              │────┐                                  
       │                                     │                              │    │ process dates, calculate averages
       │                                     │                              │<───┘                                  
       │                                     │                              │                                       
       │                                     │     Results as JSON data     │                                       
       │                                     │ <─────────────────────────────                                       
       │                                     │                              │                                       
       │ Display results (calories, spending)│                              │                                       
       │ <────────────────────────────────────                              │                                       
     ┌─┴──┐                                ┌─┴──┐                     ┌─────┴──────┐                                
     │User│                                │Main│                     │Microservice│                                
     └────┘                                └────┘                     └────────────┘                                