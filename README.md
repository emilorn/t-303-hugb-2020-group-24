**How to start the server**

    run the command "python -m src.app.WebSocketComponent.WebSocketServer" from the project root folder(t-303-hugb-2020-group-24)

**Expected format of request**

    {"op":"<function name here>", "data":"<parameter goes here>"}

    Example of this format:
        {"op":"getHistoricalPolls", "data":"2018"}

**List of supported opperations**

| function | parameter | return parameters |
| ------ | ------ | ------ |
| getAllPolls | None | [Poll] |
| getPollPerRegion | regionID:string | [Poll] |
| getCandidates | None | [CandidateDAO] |
|getCandidateDetails | candidateID:string | Candidate |
| getRegionDetails | regionID:string | Region |
| getHistoricalPolls | year:number | [Poll] |
| getElectionDetails | electionID:string | Election |
| getAllRegions | electionID:string | [Region] |
| getAveragePoll | electionID:string | Poll |
| getPollPerElection | electionID:string | [Poll] |
