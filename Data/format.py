import csv

# List of states plus District of Columbia
states = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut",
          "Delaware", "District of Columbia", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois",
          "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts",
          "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada",
          "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota",
          "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina",
          "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington",
          "West Virginia", "Wisconsin", "Wyoming"]

state_set = set(states)

# pasted data from https://www.bls.gov/charts/state-employment-and-unemployment/state-unemployment-rates-animated.htm
data = '''State	Sep 2014	Oct 2014	Nov 2014	Dec 2014	Jan 2015	Feb 2015	Mar 2015	Apr 2015	May 2015	Jun 2015	Jul 2015	Aug 2015	Sep 2015	Oct 2015	Nov 2015	Dec 2015	Jan 2016	Feb 2016	Mar 2016	Apr 2016	May 2016	Jun 2016	Jul 2016	Aug 2016	Sep 2016	Oct 2016	Nov 2016	Dec 2016	Jan 2017	Feb 2017	Mar 2017	Apr 2017	May 2017	Jun 2017	Jul 2017	Aug 2017	Sep 2017	Oct 2017	Nov 2017	Dec 2017	Jan 2018	Feb 2018	Mar 2018	Apr 2018	May 2018	Jun 2018	Jul 2018	Aug 2018	Sep 2018	Oct 2018	Nov 2018	Dec 2018	Jan 2019	Feb 2019	Mar 2019	Apr 2019	May 2019	Jun 2019	Jul 2019	Aug 2019	Sep 2019	Oct 2019	Nov 2019	Dec 2019	Jan 2020	Feb 2020	Mar 2020	Apr 2020	May 2020	Jun 2020	Jul 2020	Aug 2020	Sep 2020	Oct 2020	Nov 2020	Dec 2020	Jan 2021	Feb 2021	Mar 2021	Apr 2021	May 2021	Jun 2021	Jul 2021	Aug 2021	Sep 2021	Oct 2021	Nov 2021	Dec 2021	Jan 2022	Feb 2022	Mar 2022	Apr 2022	May 2022	Jun 2022	Jul 2022	Aug 2022	Sep 2022	Oct 2022	Nov 2022	Dec 2022	Jan 2023	Feb 2023	Mar 2023	Apr 2023	May 2023	Jun 2023	Jul 2023	Aug 2023	Sep 2023	Oct 2023	Nov 2023	Dec 2023	Jan 2024	Feb 2024	Mar 2024	Apr 2024	May 2024	Jun 2024	Jul 2024	Aug 2024	Sep 2024
Alabama

6.5	6.4	6.3	6.2	6.1	6.1	6.1	6.1	6.1	6.2	6.2	6.2	6.1	6.1	6.1	6.1	6.1	6.0	6.0	5.9	5.9	5.9	5.9	5.9	5.9	5.9	5.8	5.7	5.5	5.2	5.0	4.8	4.6	4.4	4.3	4.2	4.1	4.0	4.0	4.0	4.0	4.0	4.0	4.0	4.0	4.0	4.0	3.9	3.9	3.9	3.8	3.8	3.7	3.6	3.4	3.3	3.1	3.0	3.0	3.0	3.0	3.0	3.0	3.1	3.2	3.3	3.4	13.8	10.4	8.6	7.5	6.3	5.9	5.2	4.8	4.5	4.2	3.9	3.8	3.7	3.5	3.5	3.3	3.2	3.0	2.9	2.8	2.7	2.6	2.6	2.6	2.5	2.5	2.5	2.5	2.5	2.5	2.5	2.5	2.4	2.4	2.3	2.3	2.3	2.3	2.3	2.4	2.5	2.7	2.8	2.8	2.8	2.9	3.0	3.0	3.1	3.0	2.9	2.8	2.8	2.9
Alaska

6.7	6.5	6.4	6.3	6.2	6.3	6.3	6.3	6.3	6.3	6.2	6.2	6.2	6.3	6.3	6.4	6.4	6.5	6.5	6.5	6.6	6.6	6.6	6.7	6.7	6.7	6.7	6.7	6.6	6.6	6.5	6.5	6.5	6.5	6.5	6.5	6.5	6.5	6.5	6.4	6.4	6.3	6.2	6.1	6.0	5.9	5.9	5.9	5.9	5.9	6.0	6.0	6.0	5.9	5.8	5.7	5.6	5.6	5.6	5.6	5.5	5.4	5.3	5.3	5.4	5.5	5.5	11.7	11.8	11.2	11.1	8.6	7.9	7.3	7.1	7.1	7.0	7.0	7.0	7.0	6.8	6.8	6.4	6.2	5.9	5.7	5.5	5.3	5.2	4.8	4.5	4.3	4.2	4.1	4.0	3.8	3.9	4.0	4.0	4.0	3.9	3.9	3.8	3.9	4.0	4.1	4.3	4.4	4.5	4.6	4.6	4.6	4.6	4.6	4.6	4.6	4.5	4.5	4.5	4.6	4.6
Arizona

6.7	6.6	6.5	6.4	6.4	6.3	6.2	6.2	6.1	6.1	6.1	6.0	6.0	5.9	5.8	5.8	5.7	5.6	5.6	5.6	5.5	5.5	5.5	5.4	5.4	5.4	5.3	5.3	5.2	5.2	5.1	5.0	5.0	4.9	4.9	4.8	4.9	4.9	4.9	4.9	4.9	4.8	4.8	4.7	4.7	4.7	4.7	4.7	4.8	4.9	5.0	5.0	5.0	5.0	4.9	4.8	4.8	4.8	4.8	4.8	4.7	4.7	4.7	4.7	4.8	4.8	4.9	13.8	11.2	9.8	8.9	7.9	7.5	7.0	6.7	6.6	6.4	6.2	6.0	5.8	5.5	5.3	5.0	4.6	4.3	4.1	3.9	3.7	3.7	3.6	3.6	3.6	3.7	3.7	3.8	3.9	4.0	4.0	3.9	3.8	3.7	3.7	3.6	3.6	3.7	3.8	3.9	4.1	4.2	4.2	4.2	4.2	4.2	4.1	3.8	3.6	3.4	3.3	3.4	3.4	3.5
Arkansas

5.7	5.6	5.6	5.5	5.5	5.4	5.4	5.3	5.2	5.1	4.9	4.8	4.6	4.5	4.4	4.3	4.2	4.1	4.0	4.0	4.0	4.0	4.0	4.0	3.9	3.9	3.9	3.8	3.8	3.7	3.7	3.7	3.7	3.7	3.7	3.7	3.8	3.8	3.8	3.8	3.8	3.8	3.7	3.7	3.6	3.6	3.5	3.5	3.6	3.7	3.7	3.7	3.7	3.6	3.5	3.4	3.4	3.4	3.4	3.5	3.5	3.5	3.5	3.5	3.5	3.6	4.9	10.1	8.9	7.9	7.3	6.4	6.0	5.4	5.2	5.0	4.9	4.8	4.7	4.5	4.4	4.2	3.9	3.7	3.5	3.4	3.3	3.2	3.2	3.2	3.2	3.1	3.2	3.2	3.2	3.3	3.3	3.3	3.2	3.1	3.0	2.9	2.8	2.8	2.9	3.0	3.2	3.4	3.6	3.7	3.7	3.7	3.7	3.6	3.5	3.4	3.4	3.3	3.3	3.3	3.3
California

7.3	7.2	7.1	6.9	6.8	6.7	6.6	6.5	6.4	6.3	6.2	6.0	5.9	5.8	5.8	5.7	5.7	5.6	5.6	5.5	5.5	5.5	5.5	5.5	5.5	5.5	5.4	5.4	5.2	5.1	5.0	5.0	4.9	4.9	4.8	4.8	4.7	4.6	4.5	4.5	4.4	4.3	4.3	4.2	4.2	4.2	4.2	4.2	4.2	4.3	4.3	4.3	4.3	4.3	4.2	4.1	4.0	4.0	4.0	4.0	4.0	4.0	4.1	4.2	4.3	4.4	5.5	16.1	15.8	13.8	13.2	11.9	10.0	9.3	9.0	9.0	8.7	8.6	8.4	8.3	7.9	7.8	7.4	7.0	6.5	6.1	5.7	5.5	5.2	4.8	4.4	4.2	4.1	4.0	3.9	3.8	4.0	4.2	4.3	4.4	4.5	4.5	4.5	4.5	4.5	4.6	4.7	4.8	5.0	5.1	5.1	5.1	5.2	5.3	5.3	5.3	5.2	5.2	5.2	5.3	5.3
Colorado

4.5	4.4	4.3	4.2	4.1	4.1	4.1	4.0	3.9	3.8	3.7	3.6	3.5	3.4	3.4	3.3	3.3	3.3	3.3	3.3	3.3	3.2	3.2	3.1	3.0	3.0	2.9	2.7	2.6	2.5	2.4	2.4	2.4	2.5	2.6	2.7	2.8	2.8	2.8	2.8	2.9	2.9	2.9	3.0	3.0	3.1	3.1	3.1	3.2	3.2	3.1	3.1	3.0	2.9	2.8	2.6	2.6	2.5	2.5	2.5	2.5	2.6	2.7	2.8	3.0	3.2	3.3	11.2	11.7	11.2	6.5	6.2	6.3	6.2	6.2	6.4	6.3	6.3	6.2	6.2	5.9	5.9	5.6	5.3	4.9	4.6	4.4	4.2	4.0	3.6	3.3	3.1	3.0	2.8	2.7	2.6	2.8	2.9	3.0	3.0	3.0	3.0	3.0	3.0	3.1	3.1	3.2	3.2	3.3	3.3	3.3	3.3	3.4	3.5	3.7	3.7	3.8	3.8	3.9	4.0	4.0
Connecticut

6.4	6.3	6.2	6.1	6.0	5.9	5.8	5.8	5.7	5.6	5.6	5.5	5.4	5.4	5.4	5.3	5.2	5.2	5.1	5.0	4.9	4.9	4.8	4.7	4.7	4.7	4.6	4.6	4.6	4.5	4.5	4.5	4.4	4.4	4.4	4.4	4.4	4.3	4.3	4.3	4.2	4.1	4.1	4.0	3.9	3.9	3.8	3.8	3.7	3.7	3.7	3.7	3.7	3.6	3.6	3.5	3.5	3.5	3.5	3.6	3.6	3.6	3.7	3.7	3.8	3.8	3.9	8.3	11.8	11.5	11.7	9.6	8.8	7.9	7.5	7.4	7.1	7.1	7.0	7.1	6.9	6.8	6.5	6.2	5.9	5.6	5.3	5.1	4.9	4.6	4.4	4.3	4.1	4.0	3.9	3.8	3.8	3.8	3.8	3.7	3.6	3.5	3.4	3.3	3.3	3.4	3.6	3.8	4.0	4.2	4.2	4.2	4.4	4.5	4.5	4.4	4.3	3.9	3.6	3.4	3.2
Delaware

5.4	5.3	5.2	5.1	5.0	4.9	4.9	4.9	4.9	4.8	4.8	4.7	4.7	4.7	4.6	4.6	4.5	4.5	4.4	4.4	4.4	4.5	4.5	4.5	4.6	4.6	4.7	4.7	4.7	4.6	4.6	4.6	4.5	4.5	4.5	4.4	4.4	4.3	4.3	4.2	4.1	4.0	3.9	3.8	3.8	3.7	3.6	3.6	3.5	3.5	3.5	3.5	3.5	3.5	3.5	3.5	3.5	3.5	3.6	3.6	3.6	3.6	3.6	3.6	3.6	3.6	5.0	13.1	13.4	12.7	7.5	7.3	7.5	5.1	5.3	5.6	5.7	5.8	5.9	5.9	5.9	5.8	5.6	5.4	5.2	5.0	4.8	4.7	4.6	4.4	4.3	4.2	4.2	4.2	4.1	4.1	4.2	4.2	4.2	4.1	4.1	4.0	3.9	3.8	3.8	3.9	3.9	4.0	4.1	4.1	4.1	4.1	4.1	4.0	3.9	3.9	3.9	4.0	4.1	4.2	4.2
District of Columbia

7.6	7.6	7.5	7.4	7.4	7.3	7.2	7.2	7.0	6.9	6.8	6.8	6.7	6.6	6.6	6.5	6.4	6.3	6.2	6.1	6.1	6.1	6.2	6.2	6.3	6.3	6.3	6.3	6.3	6.2	6.2	6.2	6.2	6.1	6.1	6.1	6.0	6.0	5.9	5.9	5.9	5.8	5.8	5.8	5.7	5.6	5.5	5.5	5.5	5.6	5.7	5.8	5.9	5.9	5.8	5.7	5.6	5.4	5.4	5.3	5.2	5.2	5.2	5.4	5.5	5.7	5.8	11.2	8.8	8.6	8.6	8.4	8.4	8.1	7.9	7.7	7.3	7.1	7.0	7.1	7.1	7.3	7.1	7.0	6.6	6.5	6.3	6.1	6.0	5.6	5.2	4.9	4.7	4.4	4.2	4.0	4.2	4.4	4.6	4.8	4.9	5.0	5.0	4.9	4.8	4.8	4.7	4.8	4.9	4.9	4.9	4.9	5.0	5.1	5.2	5.2	5.3	5.4	5.5	5.7	5.7
Florida

6.2	6.1	6.0	6.0	5.9	5.8	5.8	5.7	5.7	5.6	5.5	5.4	5.3	5.3	5.2	5.1	5.1	5.0	5.0	4.9	4.9	4.9	4.9	4.9	4.9	4.9	4.8	4.8	4.7	4.6	4.5	4.4	4.3	4.3	4.2	4.2	4.2	4.1	4.1	4.0	3.9	3.9	3.8	3.8	3.7	3.6	3.6	3.5	3.5	3.5	3.5	3.5	3.5	3.5	3.4	3.3	3.3	3.3	3.2	3.2	3.2	3.1	3.0	3.0	3.0	3.0	4.1	13.4	14.2	11.8	11.8	8.8	8.1	7.1	6.6	6.4	5.9	5.6	5.4	5.2	4.9	4.9	4.6	4.4	4.1	3.9	3.8	3.6	3.5	3.3	3.2	3.1	3.0	2.9	2.8	2.8	2.8	2.9	2.8	2.8	2.8	2.8	2.8	2.7	2.8	2.8	2.9	3.0	3.0	3.1	3.1	3.1	3.1	3.1	3.2	3.3	3.3	3.3	3.3	3.3	3.3
Georgia

7.0	6.8	6.7	6.6	6.5	6.4	6.3	6.3	6.2	6.1	6.0	5.9	5.9	5.8	5.8	5.7	5.7	5.7	5.6	5.5	5.4	5.4	5.4	5.4	5.4	5.4	5.4	5.3	5.2	5.1	5.0	4.9	4.8	4.8	4.7	4.6	4.6	4.5	4.5	4.4	4.3	4.2	4.1	4.1	4.0	3.9	3.9	3.9	3.9	3.9	3.9	3.9	3.8	3.8	3.7	3.6	3.6	3.6	3.5	3.5	3.5	3.4	3.4	3.5	3.5	3.6	3.7	12.4	9.8	8.4	7.6	6.7	6.4	5.5	5.3	5.1	4.8	4.6	4.4	4.3	4.1	4.0	3.9	3.7	3.5	3.4	3.3	3.2	3.1	3.1	3.0	3.0	3.0	3.1	3.1	3.2	3.2	3.3	3.3	3.3	3.2	3.2	3.2	3.2	3.2	3.2	3.2	3.2	3.2	3.2	3.2	3.2	3.1	3.1	3.1	3.1	3.2	3.3	3.4	3.6	3.6
Hawaii

4.1	4.0	3.9	3.9	3.8	3.8	3.7	3.6	3.5	3.4	3.3	3.3	3.2	3.2	3.1	3.1	3.0	3.0	3.0	3.0	3.0	2.9	2.9	2.9	2.8	2.8	2.7	2.7	2.6	2.6	2.5	2.5	2.4	2.3	2.1	2.0	1.9	1.9	1.9	1.9	2.1	2.1	2.2	2.2	2.3	2.4	2.4	2.5	2.6	2.6	2.7	2.8	2.8	2.7	2.7	2.6	2.6	2.5	2.5	2.4	2.4	2.4	2.3	2.3	2.2	2.2	2.1	22.5	20.8	17.4	15.6	13.1	13.4	11.4	10.6	10.2	9.5	9.1	8.4	7.7	6.8	6.3	5.4	4.7	4.0	3.3	3.2	3.1	3.1	3.2	3.2	3.3	3.3	3.3	3.3	3.3	3.3	3.3	3.3	3.2	3.1	3.0	2.9	2.9	2.8	2.8	2.8	2.9	3.0	3.0	3.0	3.0	3.1	3.1	3.1	3.1	3.0	2.9	2.9	2.9	2.9
Idaho

4.0	4.0	3.9	3.9	3.8	3.9	3.9	3.9	3.9	3.9	3.9	3.9	3.9	3.8	3.8	3.8	3.8	3.8	3.7	3.7	3.7	3.7	3.7	3.7	3.6	3.6	3.6	3.5	3.5	3.4	3.3	3.2	3.2	3.1	3.1	3.2	3.2	3.2	3.1	3.1	3.0	2.9	2.9	2.8	2.8	2.8	2.8	2.8	2.8	2.9	3.0	3.0	3.0	3.0	2.9	2.9	2.8	2.8	2.9	2.9	2.9	2.9	2.8	2.8	2.8	2.8	2.7	11.8	9.1	7.5	6.6	5.4	5.0	4.4	4.2	4.2	4.1	4.1	4.0	3.9	3.7	3.6	3.5	3.4	3.3	3.1	3.0	2.9	2.8	2.7	2.7	2.7	2.7	2.8	2.9	2.9	3.0	3.0	3.0	2.9	2.9	2.9	2.9	2.9	2.9	3.0	3.1	3.2	3.3	3.3	3.3	3.3	3.3	3.3	3.3	3.3	3.3	3.4	3.5	3.5	3.6
Illinois

6.6	6.5	6.3	6.2	6.1	6.1	6.0	6.0	6.0	6.0	5.9	5.9	5.9	5.9	6.0	6.1	6.2	6.2	6.2	6.1	6.0	5.9	5.8	5.8	5.7	5.7	5.6	5.4	5.3	5.1	5.0	4.9	4.9	4.9	5.0	5.0	4.9	4.9	4.8	4.7	4.6	4.5	4.4	4.3	4.3	4.2	4.3	4.3	4.4	4.4	4.5	4.6	4.6	4.5	4.4	4.2	4.0	3.8	3.8	3.7	3.7	3.7	3.6	3.6	3.7	3.9	5.1	18.1	14.7	12.6	11.4	9.7	9.0	8.1	7.8	7.6	7.2	7.0	6.8	6.7	6.5	6.4	6.2	5.9	5.5	5.2	5.0	4.8	4.7	4.7	4.6	4.5	4.5	4.5	4.5	4.5	4.6	4.6	4.6	4.5	4.4	4.3	4.2	4.2	4.2	4.3	4.4	4.6	4.7	4.8	4.7	4.7	4.7	4.8	4.8	4.8	4.9	5.0	5.2	5.3	5.3
Indiana

5.8	5.7	5.6	5.5	5.4	5.2	5.1	4.9	4.8	4.7	4.6	4.6	4.5	4.5	4.5	4.6	4.6	4.6	4.6	4.6	4.5	4.4	4.4	4.3	4.2	4.1	4.1	4.0	3.8	3.7	3.5	3.4	3.4	3.4	3.5	3.5	3.5	3.5	3.4	3.3	3.3	3.3	3.3	3.4	3.4	3.4	3.4	3.5	3.5	3.5	3.6	3.6	3.5	3.5	3.4	3.3	3.2	3.2	3.2	3.2	3.3	3.3	3.3	3.3	3.3	3.4	3.5	16.8	12.5	10.3	8.9	7.2	6.5	5.6	5.2	5.0	4.7	4.6	4.5	4.4	4.2	4.1	3.9	3.7	3.5	3.3	3.1	3.0	2.9	2.9	2.8	2.9	2.9	3.0	3.1	3.2	3.2	3.3	3.3	3.3	3.2	3.2	3.2	3.2	3.2	3.3	3.4	3.4	3.5	3.5	3.5	3.5	3.5	3.5	3.5	3.6	3.7	3.8	4.0	4.2	4.3
Iowa

4.2	4.1	4.0	3.9	3.9	3.8	3.8	3.8	3.7	3.7	3.6	3.6	3.6	3.6	3.6	3.6	3.6	3.6	3.6	3.6	3.6	3.7	3.6	3.6	3.6	3.5	3.5	3.4	3.3	3.2	3.2	3.1	3.1	3.1	3.1	3.0	3.0	2.9	2.9	2.8	2.8	2.7	2.6	2.6	2.5	2.5	2.5	2.5	2.5	2.5	2.6	2.6	2.6	2.6	2.6	2.6	2.6	2.6	2.7	2.7	2.8	2.7	2.7	2.7	2.7	2.7	2.6	11.0	8.4	6.8	5.9	5.0	4.6	4.3	4.2	4.2	4.2	4.2	4.3	4.3	4.3	4.2	4.0	3.8	3.6	3.3	3.1	2.9	2.7	2.6	2.5	2.5	2.6	2.7	2.8	3.0	3.1	3.1	3.1	3.0	2.9	2.9	2.8	2.8	2.8	2.9	3.0	3.1	3.1	3.1	3.1	3.0	3.0	3.0	2.9	2.8	2.8	2.8	2.8	2.9	2.9
Kansas

4.4	4.3	4.3	4.3	4.3	4.4	4.4	4.4	4.3	4.2	4.1	4.0	4.0	3.9	3.9	3.9	3.9	3.9	3.9	4.0	4.0	4.0	4.1	4.1	4.1	4.1	4.1	4.0	3.9	3.8	3.7	3.6	3.6	3.6	3.6	3.6	3.6	3.5	3.5	3.4	3.5	3.4	3.4	3.4	3.3	3.3	3.3	3.3	3.3	3.3	3.4	3.4	3.3	3.3	3.2	3.2	3.2	3.1	3.1	3.1	3.1	3.1	3.1	3.1	3.1	3.1	3.1	12.1	9.1	7.4	6.7	5.8	5.4	4.9	4.7	4.4	4.0	3.8	3.7	3.6	3.6	3.5	3.4	3.3	3.1	2.9	2.7	2.6	2.5	2.5	2.5	2.5	2.5	2.6	2.6	2.7	2.7	2.8	2.8	2.8	2.8	2.8	2.7	2.7	2.6	2.6	2.6	2.6	2.6	2.6	2.6	2.6	2.6	2.7	2.7	2.8	2.9	3.0	3.2	3.3	3.3
Kentucky

5.9	5.7	5.5	5.4	5.3	5.3	5.3	5.3	5.2	5.2	5.2	5.2	5.2	5.2	5.2	5.2	5.2	5.1	5.1	5.0	4.9	4.9	4.9	5.0	5.0	5.1	5.1	5.1	5.1	5.0	5.0	5.0	4.9	4.9	4.8	4.8	4.6	4.5	4.4	4.3	4.2	4.2	4.2	4.2	4.2	4.2	4.2	4.2	4.2	4.2	4.2	4.2	4.2	4.2	4.1	4.1	4.1	4.1	4.1	4.1	4.1	4.0	4.0	4.0	4.1	4.1	4.2	16.8	12.8	5.3	5.8	5.2	5.0	4.8	4.8	4.7	4.6	4.6	4.6	4.6	4.5	4.6	4.6	4.5	4.4	4.3	4.2	4.1	4.0	4.0	3.9	3.9	4.0	4.0	4.0	4.1	4.1	4.1	4.1	4.1	4.1	4.0	4.0	4.0	4.1	4.1	4.2	4.2	4.3	4.3	4.3	4.3	4.3	4.4	4.5	4.6	4.6	4.6	4.7	4.8	4.9
Louisiana

6.7	6.8	6.8	6.8	6.8	6.7	6.6	6.5	6.4	6.3	6.1	6.1	6.0	6.0	6.0	6.0	6.0	6.1	6.1	6.1	6.1	6.1	6.1	6.1	6.1	6.1	6.0	5.9	5.8	5.7	5.5	5.4	5.2	5.1	4.9	4.8	4.8	4.7	4.7	4.7	4.7	4.7	4.8	4.9	4.9	4.9	4.9	4.9	4.8	4.8	4.8	4.8	4.7	4.6	4.5	4.4	4.4	4.4	4.6	4.7	4.8	4.8	4.8	4.8	4.8	4.7	6.7	13.5	12.3	11.0	10.4	9.2	8.7	8.0	7.6	7.4	7.0	6.8	6.6	6.4	6.1	5.9	5.5	5.2	4.8	4.5	4.3	4.1	4.0	3.8	3.7	3.6	3.6	3.5	3.5	3.5	3.6	3.6	3.6	3.6	3.7	3.6	3.5	3.4	3.4	3.3	3.4	3.6	3.8	4.0	4.0	4.0	4.1	4.2	4.4	4.3	4.1	4.0	3.9	3.9	3.9
Maine

5.3	5.2	5.2	5.0	4.9	4.8	4.7	4.6	4.5	4.4	4.3	4.2	4.1	4.1	4.0	4.0	4.0	3.9	3.9	3.9	3.8	3.8	3.8	3.7	3.7	3.7	3.6	3.5	3.5	3.4	3.4	3.4	3.4	3.4	3.4	3.4	3.4	3.3	3.2	3.1	3.1	3.0	3.0	3.0	3.1	3.2	3.3	3.3	3.3	3.3	3.3	3.2	3.1	3.0	2.9	2.8	2.7	2.7	2.8	2.8	2.9	3.0	3.1	3.1	3.2	3.2	3.2	9.3	9.5	6.6	6.3	4.2	4.0	3.8	3.9	4.2	4.4	4.7	4.9	5.1	5.0	5.1	4.9	4.8	4.6	4.4	4.2	3.9	3.7	3.3	3.0	2.8	2.7	2.6	2.6	2.5	2.7	2.8	2.8	2.7	2.5	2.4	2.4	2.4	2.5	2.6	2.8	3.0	3.2	3.4	3.4	3.4	3.4	3.4	3.3	3.1	3.0	2.8	2.8	2.8	2.8
Maryland

5.6	5.5	5.5	5.4	5.4	5.3	5.3	5.2	5.1	5.0	4.9	4.9	4.8	4.7	4.7	4.6	4.5	4.4	4.3	4.3	4.3	4.3	4.2	4.2	4.3	4.3	4.2	4.2	4.1	4.0	4.0	3.9	3.9	3.9	4.0	4.0	4.0	4.1	4.1	4.0	4.1	4.0	4.0	3.9	3.8	3.8	3.7	3.7	3.7	3.7	3.7	3.7	3.6	3.5	3.5	3.4	3.4	3.3	3.4	3.4	3.3	3.3	3.2	3.2	3.3	3.4	3.4	9.0	8.8	8.1	7.8	7.1	7.0	6.6	6.5	6.6	6.3	6.2	6.1	5.9	5.7	5.7	5.3	5.1	4.6	4.3	3.9	3.6	3.5	3.3	3.1	3.0	3.0	3.0	3.0	3.0	2.9	2.8	2.7	2.5	2.4	2.2	2.0	1.9	1.9	1.9	1.9	2.1	2.2	2.3	2.2	2.2	2.3	2.4	2.5	2.6	2.7	2.8	2.8	2.9	2.9
Massachusetts

5.6	5.5	5.4	5.2	5.2	5.1	5.0	5.0	4.9	4.8	4.7	4.7	4.6	4.6	4.5	4.4	4.4	4.3	4.2	4.1	4.1	4.0	3.9	3.9	3.9	3.9	3.9	3.9	3.8	3.8	3.8	3.8	3.8	3.8	3.8	3.8	3.8	3.8	3.8	3.7	3.7	3.7	3.6	3.6	3.5	3.5	3.4	3.4	3.4	3.3	3.3	3.3	3.2	3.2	3.1	3.1	3.0	3.0	3.0	3.0	3.0	2.9	2.9	2.9	3.0	3.0	3.0	17.4	14.9	14.5	12.6	10.4	9.7	8.5	7.9	7.6	6.9	6.5	6.2	6.1	5.7	5.7	5.3	5.1	4.7	4.5	4.2	3.9	3.9	3.8	3.6	3.6	3.7	3.6	3.6	3.7	3.6	3.7	3.6	3.5	3.5	3.6	3.5	3.2	3.3	3.3	3.2	3.3	3.3	3.4	3.3	3.2	3.0	2.9	2.9	2.9	3.0	3.2	3.5	3.7	3.8
Michigan

6.8	6.6	6.4	6.2	6.0	5.9	5.8	5.7	5.6	5.5	5.4	5.2	5.1	5.0	5.0	4.9	4.9	4.9	5.0	5.0	5.0	5.0	5.0	5.0	5.1	5.1	5.1	5.0	4.8	4.7	4.5	4.3	4.3	4.4	4.5	4.6	4.7	4.8	4.7	4.6	4.5	4.4	4.3	4.1	4.0	4.0	4.0	4.0	4.1	4.1	4.2	4.2	4.2	4.2	4.2	4.2	4.1	4.1	4.1	4.1	4.0	3.9	3.8	3.7	3.7	3.7	3.7	22.6	19.2	14.5	12.5	10.0	8.9	7.7	7.1	7.0	6.5	6.3	6.2	6.2	6.2	6.2	6.0	5.8	5.4	5.1	4.8	4.5	4.4	4.3	4.2	4.1	4.0	4.0	4.0	4.0	4.1	4.2	4.2	4.1	4.0	3.8	3.7	3.6	3.6	3.7	3.8	4.0	4.1	4.2	4.1	4.1	4.0	3.9	3.9	3.9	3.9	4.1	4.4	4.5	4.5
Minnesota

4.0	4.0	3.9	3.9	3.8	3.8	3.8	3.8	3.8	3.8	3.8	3.8	3.8	3.7	3.8	3.8	3.8	3.8	3.8	3.8	3.8	3.8	3.9	3.9	4.0	4.0	4.0	3.9	3.8	3.7	3.6	3.5	3.5	3.5	3.4	3.4	3.4	3.4	3.3	3.3	3.1	3.1	3.0	3.0	2.9	2.9	2.9	2.9	3.0	3.1	3.2	3.2	3.3	3.3	3.3	3.2	3.2	3.2	3.2	3.3	3.3	3.3	3.3	3.4	3.4	3.5	3.6	8.9	11.2	8.9	7.9	6.7	6.1	5.4	5.0	4.8	4.4	4.2	4.1	4.0	3.9	3.8	3.7	3.6	3.4	3.3	3.1	2.9	2.7	2.5	2.4	2.3	2.3	2.3	2.4	2.5	2.7	2.7	2.8	2.8	2.8	2.8	2.8	2.8	2.9	2.9	3.0	2.9	2.8	2.8	2.7	2.7	2.7	2.7	2.7	2.7	2.8	2.9	3.2	3.3	3.4
Mississippi

7.4	7.2	7.1	6.9	6.8	6.7	6.7	6.6	6.5	6.4	6.3	6.3	6.3	6.4	6.4	6.4	6.3	6.2	6.1	6.0	6.0	5.9	5.9	5.9	5.9	5.9	5.8	5.7	5.6	5.5	5.4	5.4	5.3	5.3	5.2	5.2	5.1	5.0	4.9	4.9	4.9	4.9	4.9	4.9	4.9	4.8	4.8	4.9	4.9	5.1	5.2	5.3	5.4	5.4	5.4	5.4	5.4	5.5	5.6	5.7	5.6	5.6	5.5	5.5	5.6	5.8	5.9	15.6	11.2	9.4	8.3	7.4	7.1	6.8	6.7	6.6	6.5	6.3	6.2	6.1	5.9	5.7	5.5	5.2	4.9	4.6	4.4	4.2	4.1	3.9	3.8	3.7	3.7	3.7	3.7	3.8	3.8	3.8	3.8	3.6	3.5	3.3	3.2	3.1	3.1	3.1	3.1	3.2	3.2	3.2	3.2	3.2	3.2	3.1	3.0	2.8	2.8	2.8	2.7	2.7	2.8
Missouri

5.9	5.8	5.7	5.7	5.6	5.6	5.6	5.5	5.3	5.2	5.0	4.9	4.8	4.7	4.6	4.5	4.5	4.4	4.4	4.5	4.6	4.7	4.7	4.7	4.7	4.6	4.5	4.3	4.2	4.1	3.9	3.8	3.7	3.7	3.6	3.6	3.6	3.6	3.6	3.5	3.6	3.5	3.4	3.3	3.2	3.1	3.1	3.0	3.1	3.1	3.2	3.3	3.3	3.3	3.2	3.2	3.1	3.1	3.1	3.2	3.3	3.4	3.4	3.4	3.4	3.4	3.5	11.6	9.6	8.0	7.2	6.4	5.9	5.4	5.2	5.0	4.9	4.8	4.8	4.7	4.5	4.3	4.1	3.9	3.7	3.5	3.3	3.2	3.0	2.7	2.5	2.4	2.3	2.3	2.4	2.5	2.7	2.8	2.8	2.8	2.8	2.8	2.8	2.9	2.9	3.0	3.1	3.2	3.3	3.3	3.3	3.3	3.3	3.3	3.3	3.4	3.5	3.7	3.8	3.9	3.9
Montana

4.6	4.5	4.5	4.4	4.3	4.3	4.3	4.2	4.3	4.3	4.3	4.3	4.3	4.3	4.3	4.3	4.4	4.4	4.4	4.4	4.4	4.3	4.3	4.3	4.3	4.3	4.2	4.2	4.2	4.1	4.1	4.1	4.1	4.1	4.1	4.1	4.1	4.1	4.0	4.0	4.0	3.9	3.8	3.8	3.7	3.7	3.7	3.7	3.7	3.7	3.7	3.6	3.6	3.6	3.5	3.5	3.4	3.4	3.5	3.5	3.5	3.5	3.5	3.5	3.6	3.5	3.5	12.0	9.2	7.6	6.7	5.6	5.2	4.6	4.4	4.2	4.0	3.9	3.8	3.7	3.6	3.5	3.4	3.3	3.1	3.0	2.8	2.7	2.7	2.6	2.6	2.7	2.7	2.7	2.8	2.8	2.7	2.7	2.6	2.6	2.5	2.5	2.5	2.6	2.6	2.7	2.8	3.0	3.2	3.3	3.3	3.3	3.3	3.4	3.3	3.1	3.1	3.1	3.1	3.2	3.3
Nebraska

3.1	3.1	3.0	3.0	2.9	2.9	3.0	3.0	3.0	3.0	3.0	3.0	3.0	3.0	3.0	3.0	3.0	3.0	3.0	3.0	3.0	3.1	3.1	3.1	3.1	3.2	3.1	3.1	3.1	3.0	3.0	2.9	2.9	2.9	2.9	3.0	3.0	3.0	3.0	3.0	2.9	2.9	2.9	2.9	2.8	2.9	2.9	2.9	2.9	3.0	3.0	3.1	3.1	3.1	3.1	3.1	3.1	3.1	3.1	3.2	3.2	3.2	3.1	3.1	3.0	3.0	4.4	8.2	6.4	5.2	4.6	3.9	3.5	3.1	3.0	3.0	2.9	2.9	2.9	2.8	2.7	2.7	2.6	2.5	2.4	2.3	2.2	2.1	2.0	2.0	1.9	1.9	2.0	2.1	2.2	2.3	2.4	2.4	2.3	2.2	2.1	2.1	2.0	2.0	2.1	2.2	2.3	2.4	2.5	2.5	2.5	2.5	2.5	2.5	2.5	2.5	2.5	2.6	2.6	2.7	2.7
Nevada

7.8	7.7	7.6	7.5	7.4	7.3	7.2	7.1	7.0	6.9	6.8	6.7	6.6	6.5	6.4	6.3	6.2	6.2	6.1	6.0	5.9	5.8	5.7	5.7	5.6	5.6	5.5	5.4	5.4	5.3	5.2	5.1	5.0	4.9	4.8	4.8	4.8	4.8	4.8	4.9	4.7	4.6	4.6	4.5	4.4	4.3	4.2	4.2	4.2	4.3	4.3	4.3	4.3	4.3	4.2	4.2	4.1	4.1	4.0	4.1	4.1	4.1	4.1	4.2	4.2	4.4	7.3	30.6	24.7	18.9	16.7	13.9	12.7	11.2	10.3	9.7	8.9	8.5	8.0	7.6	7.2	6.9	6.5	6.2	5.9	5.6	5.4	5.3	5.2	5.2	5.1	5.1	5.1	5.1	5.2	5.2	5.3	5.3	5.3	5.3	5.2	5.2	5.1	5.0	5.0	5.0	5.0	5.1	5.2	5.3	5.3	5.3	5.3	5.2	5.1	5.1	5.1	5.2	5.4	5.5	5.6
New Hampshire

4.1	4.1	4.0	3.9	3.8	3.8	3.7	3.6	3.5	3.4	3.3	3.3	3.2	3.1	3.0	3.0	2.9	2.9	2.8	2.8	2.9	2.9	2.9	2.9	2.9	2.9	2.9	2.9	2.9	2.9	2.8	2.8	2.8	2.7	2.8	2.8	2.8	2.8	2.8	2.8	2.7	2.7	2.7	2.7	2.7	2.6	2.6	2.6	2.5	2.5	2.6	2.6	2.6	2.6	2.6	2.6	2.5	2.5	2.5	2.6	2.6	2.6	2.6	2.6	2.6	2.6	2.6	16.0	11.8	9.6	8.3	6.7	6.1	5.2	4.8	4.6	4.2	4.1	4.0	3.9	3.7	3.6	3.4	3.2	3.0	2.8	2.6	2.4	2.3	2.3	2.2	2.2	2.2	2.2	2.3	2.3	2.4	2.4	2.3	2.2	2.0	1.9	1.8	1.8	1.8	2.0	2.1	2.3	2.5	2.6	2.6	2.6	2.6	2.6	2.6	2.6	2.5	2.5	2.5	2.6	2.5
New Jersey

6.6	6.5	6.5	6.4	6.3	6.3	6.2	6.1	6.0	5.8	5.6	5.5	5.3	5.2	5.1	5.0	5.0	5.0	5.0	5.0	5.0	5.0	5.0	5.0	4.9	4.9	4.8	4.7	4.6	4.5	4.5	4.4	4.5	4.5	4.5	4.6	4.6	4.6	4.6	4.5	4.4	4.4	4.3	4.2	4.1	4.0	4.0	3.9	3.8	3.7	3.7	3.6	3.5	3.4	3.3	3.2	3.2	3.2	3.3	3.4	3.6	3.7	3.8	3.9	4.0	4.1	4.1	15.0	15.4	14.5	14.4	13.3	7.4	7.1	7.2	7.2	7.3	7.3	7.2	7.2	7.0	7.2	6.9	6.8	6.3	6.0	5.7	5.6	5.2	4.7	4.3	4.1	3.8	3.6	3.3	3.1	3.3	3.5	3.7	3.8	3.9	4.0	4.0	4.1	4.2	4.4	4.5	4.7	4.8	4.8	4.8	4.8	4.8	4.8	4.8	4.7	4.6	4.6	4.7	4.8	4.7
New Mexico

6.5	6.4	6.4	6.4	6.5	6.6	6.7	6.7	6.7	6.7	6.6	6.6	6.6	6.5	6.5	6.5	6.5	6.5	6.6	6.6	6.7	6.8	6.9	6.9	6.9	6.9	6.9	6.8	6.7	6.6	6.5	6.4	6.2	6.1	6.0	5.8	5.7	5.6	5.5	5.4	5.2	5.1	4.9	4.8	4.7	4.7	4.7	4.8	4.9	5.0	5.1	5.2	5.1	5.1	5.0	5.0	4.9	4.9	4.9	4.9	4.9	4.9	4.9	5.0	5.1	5.3	5.9	9.0	9.3	9.0	9.0	8.6	8.7	8.4	8.4	8.4	8.2	8.2	8.0	7.9	7.5	7.4	7.1	6.8	6.3	6.0	5.8	5.6	5.4	5.0	4.6	4.4	4.1	3.9	3.6	3.4	3.5	3.6	3.6	3.6	3.6	3.6	3.6	3.6	3.6	3.6	3.7	3.8	3.9	4.0	4.0	4.0	4.0	3.9	3.8	3.8	3.8	3.9	4.0	4.1	4.2
New York

6.0	5.9	5.8	5.8	5.7	5.6	5.6	5.5	5.4	5.3	5.2	5.0	4.9	4.9	4.9	4.8	4.8	4.8	4.8	4.8	4.8	4.9	4.9	5.0	5.0	5.0	4.9	4.8	4.7	4.6	4.6	4.6	4.6	4.6	4.7	4.7	4.7	4.7	4.6	4.5	4.5	4.4	4.3	4.2	4.1	4.0	3.9	3.9	3.9	4.0	4.0	4.0	4.0	3.9	3.9	3.8	3.7	3.7	3.8	3.8	3.9	3.9	3.9	4.0	4.1	4.1	4.2	15.6	16.7	13.6	12.5	10.8	10.2	9.2	9.0	8.7	8.6	8.4	8.1	7.9	7.5	7.5	7.0	6.8	6.3	5.9	5.6	5.5	5.2	4.8	4.6	4.4	4.3	4.2	4.0	3.9	4.0	4.1	4.2	4.2	4.1	4.0	4.0	3.9	3.9	4.0	4.1	4.3	4.4	4.6	4.6	4.6	4.5	4.4	4.3	4.2	4.2	4.2	4.3	4.4	4.4
North Carolina

6.0	5.9	5.8	5.7	5.7	5.7	5.8	5.8	5.8	5.8	5.7	5.7	5.6	5.5	5.4	5.4	5.3	5.2	5.2	5.1	5.1	5.0	5.0	5.1	5.1	5.1	5.0	5.0	4.9	4.7	4.6	4.5	4.5	4.5	4.5	4.5	4.5	4.4	4.4	4.3	4.2	4.1	4.0	4.0	3.9	3.9	3.9	3.9	4.0	4.0	4.0	4.0	4.0	4.0	3.9	3.9	3.8	3.9	3.9	3.9	3.9	3.8	3.8	3.8	3.8	3.8	4.0	14.2	11.6	9.7	8.7	7.3	6.7	6.0	5.8	5.8	5.6	5.5	5.4	5.3	5.2	5.1	4.9	4.8	4.5	4.3	4.1	3.9	3.7	3.6	3.5	3.5	3.6	3.6	3.7	3.8	3.9	3.8	3.8	3.7	3.5	3.4	3.3	3.3	3.3	3.4	3.4	3.5	3.6	3.6	3.6	3.6	3.5	3.5	3.5	3.5	3.6	3.6	3.7	3.8	3.8
North Dakota

2.6	2.6	2.6	2.6	2.6	2.6	2.7	2.8	2.8	2.8	2.8	2.8	2.8	2.8	2.9	3.0	3.1	3.2	3.2	3.2	3.2	3.2	3.1	3.1	3.0	3.0	3.0	2.9	2.9	2.8	2.7	2.6	2.5	2.5	2.5	2.5	2.5	2.6	2.6	2.6	2.6	2.6	2.6	2.5	2.4	2.3	2.3	2.3	2.3	2.3	2.3	2.4	2.3	2.3	2.3	2.2	2.1	2.1	2.1	2.1	2.1	2.1	2.0	2.0	2.0	2.2	2.4	8.7	7.3	6.4	6.1	5.5	5.2	4.8	4.5	4.3	4.0	3.8	3.6	3.4	3.2	3.0	2.8	2.7	2.5	2.4	2.3	2.3	2.2	2.1	2.0	2.0	1.9	1.9	1.9	2.0	2.0	2.0	2.0	2.0	2.0	2.0	1.9	1.9	1.8	1.8	1.8	1.8	1.9	1.9	1.9	1.9	1.9	2.0	2.0	2.0	2.0	2.1	2.2	2.3	2.3
Ohio

5.5	5.4	5.3	5.2	5.2	5.2	5.2	5.1	5.0	4.9	4.8	4.8	4.7	4.8	4.8	4.9	5.0	5.0	5.0	5.0	5.0	5.0	5.0	5.0	5.1	5.2	5.3	5.3	5.3	5.2	5.1	5.1	5.0	5.0	5.0	4.9	4.9	4.8	4.7	4.6	4.6	4.6	4.6	4.5	4.5	4.5	4.4	4.4	4.4	4.5	4.5	4.5	4.4	4.2	4.1	4.0	4.0	4.0	4.1	4.2	4.2	4.3	4.3	4.3	4.4	4.6	4.8	16.5	12.8	10.9	9.8	8.3	7.6	6.8	6.4	6.3	6.0	5.9	5.8	5.7	5.5	5.3	5.1	4.9	4.7	4.5	4.3	4.2	4.1	4.0	3.9	3.9	3.9	3.9	4.0	4.1	4.1	4.1	4.0	3.9	3.8	3.7	3.5	3.4	3.3	3.3	3.4	3.5	3.6	3.6	3.6	3.6	3.7	3.7	3.8	4.0	4.2	4.4	4.5	4.5	4.5
Oklahoma

4.1	4.1	4.0	4.0	4.0	4.1	4.2	4.3	4.4	4.4	4.4	4.3	4.3	4.3	4.4	4.4	4.5	4.5	4.6	4.7	4.7	4.8	4.8	4.8	4.7	4.7	4.6	4.5	4.4	4.3	4.2	4.1	4.0	4.0	4.0	4.0	3.9	3.9	3.8	3.8	3.7	3.6	3.5	3.4	3.3	3.2	3.1	3.1	3.1	3.1	3.2	3.2	3.2	3.2	3.1	3.1	3.0	3.0	3.1	3.2	3.2	3.2	3.1	3.1	3.1	3.2	3.2	12.5	9.8	8.2	7.4	6.3	6.0	5.5	5.3	5.2	5.0	4.9	4.8	4.7	4.5	4.3	4.0	3.7	3.4	3.2	3.0	2.9	2.9	2.9	2.9	2.9	2.9	3.0	3.1	3.2	3.2	3.2	3.2	3.1	3.1	3.0	3.0	2.9	3.0	3.1	3.2	3.3	3.5	3.5	3.5	3.5	3.5	3.6	3.5	3.5	3.5	3.4	3.5	3.4	3.4
Oregon

6.4	6.3	6.2	6.0	5.8	5.8	5.7	5.7	5.6	5.5	5.5	5.4	5.3	5.2	5.1	5.0	4.9	4.9	4.9	4.9	4.9	4.9	4.9	4.8	4.7	4.5	4.4	4.3	4.1	4.0	3.9	3.9	4.0	4.0	4.1	4.1	4.2	4.2	4.1	4.1	4.1	4.0	4.0	3.9	3.9	3.8	3.9	4.0	4.1	4.2	4.3	4.3	4.2	4.1	4.0	3.9	3.8	3.7	3.7	3.6	3.5	3.4	3.4	3.4	3.5	3.6	3.7	13.7	11.8	10.2	9.2	8.0	7.5	6.8	6.6	6.6	6.4	6.2	6.1	5.9	5.6	5.4	5.0	4.7	4.4	4.2	4.0	3.9	3.9	3.7	3.7	3.7	3.7	3.8	3.9	4.0	4.2	4.2	4.2	4.0	3.8	3.6	3.5	3.4	3.4	3.5	3.6	3.8	3.9	4.0	4.0	4.0	4.1	4.2	4.2	4.2	4.2	4.1	4.1	4.0	4.0
Pennsylvania

5.6	5.6	5.5	5.5	5.5	5.5	5.5	5.5	5.5	5.4	5.4	5.3	5.3	5.3	5.2	5.3	5.3	5.3	5.3	5.4	5.4	5.4	5.4	5.4	5.4	5.3	5.3	5.2	5.2	5.1	5.1	5.0	5.0	4.9	4.9	4.9	4.9	4.9	4.9	4.9	4.8	4.7	4.6	4.5	4.4	4.3	4.3	4.3	4.2	4.3	4.3	4.3	4.3	4.3	4.3	4.3	4.2	4.2	4.2	4.3	4.3	4.4	4.4	4.4	4.5	4.7	4.9	16.1	12.9	11.3	10.4	9.3	8.8	8.1	7.9	7.6	7.4	7.1	6.8	6.6	6.3	6.1	5.9	5.6	5.2	4.9	4.7	4.5	4.3	4.2	4.2	4.1	4.1	4.1	4.0	4.0	4.0	3.9	3.9	3.8	3.8	3.7	3.5	3.4	3.3	3.2	3.2	3.3	3.3	3.4	3.4	3.4	3.4	3.4	3.4	3.4	3.4	3.4	3.4	3.4	3.4
Rhode Island

7.3	7.1	6.9	6.7	6.6	6.5	6.4	6.3	6.2	6.0	5.9	5.8	5.7	5.7	5.6	5.6	5.6	5.5	5.4	5.4	5.4	5.3	5.3	5.2	5.1	5.0	4.9	4.8	4.6	4.5	4.5	4.4	4.4	4.4	4.5	4.5	4.6	4.6	4.6	4.5	4.5	4.4	4.2	4.1	4.0	3.9	3.9	3.9	3.9	3.9	3.9	3.8	3.8	3.7	3.6	3.5	3.5	3.5	3.5	3.5	3.5	3.4	3.4	3.5	3.6	3.7	3.7	17.9	15.4	13.3	12.2	10.3	9.9	7.0	7.0	6.9	6.6	6.4	6.2	6.2	6.0	6.0	5.8	5.5	5.1	4.6	4.1	3.7	3.5	3.3	3.1	3.0	3.0	3.1	3.2	3.3	3.2	3.2	3.1	3.0	2.9	2.8	2.7	2.7	2.6	2.6	2.7	2.9	3.2	3.4	3.4	3.4	3.6	3.9	4.1	4.1	4.3	4.3	4.5	4.6	4.6
South Carolina

6.5	6.6	6.5	6.5	6.4	6.4	6.3	6.2	6.1	6.0	5.8	5.7	5.6	5.5	5.4	5.4	5.3	5.3	5.2	5.1	5.1	5.0	4.9	4.8	4.7	4.6	4.5	4.5	4.4	4.3	4.2	4.2	4.1	4.1	4.2	4.2	4.2	4.2	4.2	4.1	3.9	3.7	3.5	3.3	3.2	3.2	3.3	3.3	3.3	3.3	3.3	3.2	3.2	3.2	3.1	3.1	2.9	2.7	2.6	2.5	2.4	2.4	2.5	2.6	2.8	2.9	3.1	11.8	9.2	7.8	7.0	6.1	5.8	5.3	5.0	4.8	4.6	4.4	4.3	4.2	4.1	4.1	3.9	3.8	3.7	3.5	3.4	3.3	3.3	3.2	3.2	3.2	3.2	3.2	3.2	3.2	3.3	3.2	3.2	3.1	3.1	3.0	3.0	2.9	2.9	2.8	2.8	2.9	3.0	3.0	3.0	3.0	3.0	3.1	3.1	3.2	3.4	3.6	3.9	4.3	4.5
South Dakota

3.3	3.3	3.2	3.2	3.2	3.2	3.2	3.1	3.1	3.1	3.1	3.0	3.0	2.9	2.9	2.8	2.8	2.8	2.8	2.9	2.9	3.0	3.1	3.1	3.2	3.2	3.2	3.2	3.1	3.1	3.1	3.0	3.0	3.0	3.1	3.1	3.1	3.0	3.0	3.0	3.0	2.9	2.9	2.8	2.8	2.8	2.7	2.7	2.7	2.7	2.7	2.8	2.8	2.8	2.8	2.8	2.8	2.8	2.8	2.8	2.8	2.7	2.7	2.6	2.6	2.5	2.4	8.8	6.6	5.3	4.7	4.0	3.7	3.3	3.2	3.1	2.9	2.9	2.8	2.8	2.8	2.8	2.7	2.6	2.5	2.3	2.2	2.1	2.0	1.9	1.9	1.9	1.9	2.0	2.0	2.1	2.1	2.1	2.0	2.0	2.0	1.9	1.9	1.9	1.9	2.0	2.0	2.0	2.1	2.1	2.1	2.1	2.1	2.1	2.1	2.0	2.0	2.0	2.0	2.0	2.0
Tennessee

6.5	6.4	6.3	6.2	6.1	6.1	6.0	5.9	5.8	5.7	5.5	5.4	5.3	5.1	5.0	4.9	4.8	4.7	4.7	4.6	4.7	4.7	4.8	4.8	4.9	4.9	4.8	4.7	4.6	4.4	4.2	3.9	3.7	3.6	3.5	3.4	3.4	3.4	3.4	3.5	3.5	3.5	3.5	3.5	3.5	3.5	3.5	3.5	3.5	3.5	3.5	3.5	3.5	3.4	3.4	3.4	3.3	3.2	3.2	3.2	3.3	3.3	3.4	3.4	3.5	3.5	3.5	15.8	12.1	10.2	9.0	7.6	7.1	6.3	5.9	5.6	5.4	5.2	5.1	5.0	4.8	4.7	4.4	4.2	3.9	3.8	3.6	3.5	3.4	3.4	3.3	3.3	3.3	3.3	3.3	3.4	3.4	3.5	3.5	3.5	3.4	3.3	3.2	3.1	3.1	3.1	3.2	3.3	3.4	3.5	3.5	3.4	3.5	3.3	3.2	3.1	3.0	3.0	3.0	3.1	3.2
Texas

5.0	4.9	4.8	4.6	4.6	4.5	4.5	4.5	4.4	4.4	4.4	4.5	4.5	4.5	4.5	4.5	4.5	4.4	4.5	4.5	4.6	4.7	4.7	4.7	4.8	4.8	4.8	4.8	4.8	4.7	4.6	4.5	4.4	4.3	4.2	4.2	4.1	4.1	4.1	4.1	4.1	4.0	4.0	4.0	3.9	3.9	3.9	3.8	3.8	3.8	3.8	3.8	3.7	3.7	3.6	3.5	3.4	3.4	3.5	3.5	3.5	3.5	3.5	3.5	3.5	3.6	5.0	12.8	11.6	10.1	9.3	8.1	7.7	7.1	7.0	6.9	6.7	6.6	6.4	6.2	6.0	5.8	5.6	5.3	5.1	4.9	4.6	4.5	4.3	4.1	3.9	3.8	3.8	3.8	3.8	3.8	3.9	4.0	4.0	4.1	4.1	4.0	4.0	4.0	4.0	3.9	3.9	3.9	3.9	3.9	3.9	3.9	3.9	3.9	3.9	4.0	4.0	4.0	4.1	4.1	4.1
Utah

3.6	3.6	3.6	3.6	3.6	3.5	3.5	3.5	3.5	3.5	3.5	3.5	3.5	3.5	3.5	3.5	3.5	3.5	3.5	3.4	3.4	3.4	3.3	3.3	3.3	3.2	3.2	3.2	3.2	3.2	3.2	3.2	3.2	3.2	3.2	3.2	3.1	3.1	3.1	3.1	3.0	3.0	3.0	2.9	2.9	2.9	2.9	2.9	2.9	2.9	2.9	2.8	2.8	2.7	2.7	2.6	2.6	2.5	2.5	2.5	2.4	2.4	2.4	2.4	2.5	2.5	2.5	10.0	7.7	6.4	5.7	4.9	4.5	4.0	3.8	3.6	3.4	3.2	3.1	3.0	2.9	2.8	2.7	2.6	2.5	2.4	2.3	2.2	2.2	2.2	2.2	2.3	2.3	2.3	2.4	2.4	2.5	2.5	2.5	2.5	2.5	2.5	2.5	2.5	2.5	2.6	2.7	2.7	2.8	2.8	2.8	2.8	2.8	2.8	2.8	2.8	2.9	3.0	3.2	3.3	3.5
Vermont

4.0	4.0	3.9	3.9	3.8	3.7	3.7	3.6	3.6	3.5	3.5	3.5	3.4	3.4	3.4	3.3	3.2	3.2	3.2	3.1	3.1	3.1	3.1	3.1	3.1	3.1	3.1	3.1	3.1	3.1	3.1	3.1	3.0	3.0	2.9	2.9	2.9	3.0	3.0	3.0	2.8	2.7	2.7	2.6	2.5	2.4	2.4	2.3	2.3	2.4	2.4	2.3	2.3	2.2	2.1	2.0	2.0	1.9	2.0	2.0	2.1	2.1	2.1	2.0	2.0	2.1	2.4	14.1	9.5	7.8	6.7	5.5	4.9	4.4	4.2	4.3	4.4	4.4	4.4	4.2	3.9	3.7	3.4	3.2	3.1	2.9	2.8	2.6	2.4	2.3	2.2	2.2	2.2	2.2	2.3	2.4	2.5	2.5	2.4	2.3	2.1	1.9	1.8	1.7	1.7	1.8	1.9	2.1	2.2	2.3	2.3	2.3	2.3	2.3	2.2	2.1	2.1	2.1	2.1	2.2	2.2
Virginia

5.0	4.9	4.9	4.8	4.8	4.7	4.7	4.6	4.5	4.4	4.3	4.2	4.1	4.1	4.0	4.0	4.0	3.9	3.9	3.9	3.9	4.0	4.0	4.1	4.1	4.1	4.1	4.0	4.0	4.0	3.9	3.8	3.7	3.7	3.6	3.5	3.5	3.5	3.4	3.4	3.4	3.3	3.2	3.1	2.9	2.8	2.8	2.8	2.8	2.9	3.0	3.1	3.1	3.1	3.0	2.8	2.7	2.5	2.5	2.5	2.6	2.7	2.8	2.8	2.8	2.9	3.2	12.0	10.0	8.9	8.2	7.2	6.6	5.8	5.3	5.0	4.8	4.7	4.5	4.4	4.2	4.0	3.8	3.5	3.3	3.1	3.0	2.9	2.8	2.7	2.7	2.6	2.5	2.5	2.6	2.7	2.8	3.0	3.1	3.1	3.1	3.0	2.9	2.7	2.6	2.6	2.6	2.7	2.9	3.0	3.1	3.0	3.0	3.0	2.9	2.8	2.7	2.7	2.7	2.8	2.9
Washington

5.8	5.8	5.7	5.7	5.6	5.5	5.5	5.4	5.4	5.4	5.4	5.4	5.4	5.4	5.4	5.4	5.4	5.4	5.4	5.3	5.3	5.3	5.3	5.2	5.1	5.1	5.0	4.9	4.8	4.7	4.6	4.6	4.6	4.6	4.6	4.6	4.7	4.7	4.6	4.6	4.6	4.6	4.5	4.4	4.3	4.3	4.3	4.3	4.3	4.4	4.5	4.6	4.7	4.6	4.5	4.4	4.3	4.2	4.1	4.1	4.0	3.9	3.8	3.7	3.7	3.8	5.2	16.7	13.4	11.5	10.4	8.8	8.1	7.2	6.9	6.7	6.4	6.2	6.0	5.7	5.5	5.4	5.2	5.0	4.7	4.5	4.2	4.1	4.0	4.0	3.9	3.9	3.9	4.0	4.0	4.1	4.2	4.3	4.3	4.2	4.1	4.0	3.9	3.8	3.8	3.8	3.9	4.1	4.3	4.4	4.4	4.4	4.6	4.7	4.8	4.8	4.9	4.8	4.9	4.8	4.8
West Virginia

6.4	6.4	6.3	6.4	6.4	6.5	6.7	6.8	6.8	6.8	6.7	6.6	6.5	6.4	6.4	6.4	6.4	6.3	6.3	6.2	6.2	6.2	6.1	6.1	6.0	5.9	5.8	5.6	5.4	5.2	5.1	5.0	5.0	5.1	5.1	5.2	5.3	5.3	5.4	5.4	5.4	5.4	5.3	5.3	5.2	5.1	5.1	5.0	5.0	5.0	5.1	5.1	5.0	4.9	4.8	4.8	4.7	4.8	4.8	4.9	5.0	5.1	5.1	5.2	5.3	5.3	5.4	15.8	12.4	10.5	9.4	8.1	7.5	6.9	6.5	6.3	6.1	6.0	5.9	5.7	5.5	5.4	5.1	4.9	4.6	4.4	4.2	4.0	3.9	3.8	3.8	3.8	3.8	3.9	4.0	4.0	4.0	4.0	3.8	3.7	3.6	3.5	3.5	3.5	3.6	3.8	4.0	4.2	4.3	4.3	4.3	4.3	4.3	4.3	4.3	4.3	4.2	4.1	4.2	4.2	4.2
Wisconsin

5.0	5.0	4.9	4.8	4.7	4.7	4.6	4.6	4.5	4.4	4.4	4.3	4.3	4.2	4.2	4.2	4.1	4.1	4.0	4.0	4.0	3.9	3.9	3.9	3.9	3.8	3.7	3.6	3.5	3.4	3.3	3.3	3.2	3.3	3.3	3.3	3.2	3.2	3.1	3.0	2.9	2.9	2.9	3.0	3.0	3.0	3.0	3.0	3.0	3.0	3.0	3.0	3.1	3.1	3.1	3.2	3.2	3.2	3.3	3.3	3.3	3.3	3.2	3.2	3.1	3.1	3.0	14.0	10.6	8.7	7.7	6.4	5.8	5.2	5.0	4.9	4.7	4.6	4.4	4.3	4.1	4.0	3.8	3.6	3.4	3.3	3.1	3.0	3.0	2.9	2.9	2.9	2.9	2.9	2.9	2.9	3.0	2.9	2.8	2.7	2.7	2.6	2.6	2.7	2.9	3.0	3.2	3.3	3.4	3.4	3.4	3.4	3.2	3.0	3.0	2.9	2.9	2.9	3.0	2.9	2.9
Wyoming

4.4	4.3	4.1	4.0	3.9	3.9	4.0	4.1	4.2	4.2	4.2	4.2	4.3	4.3	4.5	4.7	5.0	5.3	5.5	5.7	5.7	5.6	5.4	5.3	5.2	5.2	5.1	5.0	4.8	4.6	4.4	4.2	4.1	4.1	4.2	4.3	4.3	4.3	4.3	4.3	4.2	4.2	4.1	4.0	4.0	4.0	4.0	4.1	4.1	4.1	4.0	3.9	3.7	3.6	3.5	3.5	3.5	3.5	3.6	3.7	3.8	3.9	4.0	4.2	4.4	4.6	4.8	5.1	8.7	7.3	6.8	6.2	5.9	5.6	5.5	5.4	5.3	5.3	5.2	5.0	4.9	4.7	4.5	4.3	4.1	3.9	3.7	3.6	3.5	3.4	3.3	3.3	3.3	3.4	3.4	3.5	3.5	3.5	3.5	3.4	3.3	3.1	3.0	2.8	2.8	2.8	2.8	2.8	2.9	2.9	2.9	2.9	2.8	2.8	2.8	2.8	2.9	2.9	2.9	3.0	3.1
'''

data_lines = data.strip().splitlines()

# Get the header line
header_line = data_lines[0]
columns = header_line.split('\t')
num_months = len(columns) - 1

data_dict = {}
current_state = None

for line in data_lines[1:]:
    line = line.strip()
    if not line:
        continue 

    if line in state_set:
        current_state = line
        data_dict[current_state] = []
    else:
        data_points = line.split('\t')
        data_points = [dp.strip() for dp in data_points]

        for dp in data_points:
            if dp:
                try:
                    value = float(dp)
                    formatted_value = f"{value:.1f}"
                    data_dict[current_state].append(formatted_value)
                except ValueError:
                    print(f"Warning: Invalid data point '{dp}' for state {current_state}")
                    data_dict[current_state].append('')
            else:
                data_dict[current_state].append('')

# Check if each state has the correct number of data points
for state in data_dict:
    if len(data_dict[state]) != num_months:
        print(f"Warning: state {state} has {len(data_dict[state])} data points, expected {num_months}")

# Write to CSV file
with open('unemployment.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(columns)
    for state in states:
        if state in data_dict:
            row = [state] + data_dict[state]
            writer.writerow(row)
        else:
            print(f"Warning: No data for state {state}")