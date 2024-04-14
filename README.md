# NYC Citibikes Dashboard
Thanks to [DataTalksClub](https://github.com/DataTalksClub) for creating this program and offering it for free, a truly impressive initiative!
## **Overview of the Project**
This repository represents the completion of the [data engineering zoomcamp 2024](https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main) course. \
The project investigates the [NYC Citibike rides in February 2016](https://s3.amazonaws.com/tripdata/JC-201602-citibike-tripdata.csv.zip), which documents bike rides taken in New York City using the Citibike bike-sharing system to gain insights and conduct analysis.
## **Goal**
The goal is to analyze the usage trends of the Citibike system in NYC to identify patterns that could influence future transportation planning decisions. Specifically, the project aims to answer the following questions:
- Which Citibike stations are the most popular?
- What time of day are most trips usually taken?
- On which days of the week are the most trips recorded?
## **Setup**
To set up the project, follow the steps below, ensuring you have the necessary tools and credentials:
   - Clone the project's GitHub repository to your local machine:
     ```
     git clone https://github.com/mturky56/dezoomcamp-capstone-project.git
   - Start the docker containers for MageAI and its Postgres database with the command:
     ```
     docker-compose -f mageai/docker-compose.yml up -d
   - Move the `citibikes_pipeline` to the `mageai/pipelines` directory to deploy the pre-made pipeline in MageAI.
   - Once a remote SSH connection is established to your VM through VS Code with port 6789 forwarded, access the MageAI server instance at [http://localhost:6789](http://localhost:6789) and run `citibikes_pipeline`.
   - Install dbt cloud to carry out transformations and analysis using the data.
## **Technological Resources**
State-of-the-art technologies have been utilized in the project to build a sturdy, scalable data pipeline. These technologies include:
- **[Google Cloud Storage Data lake (GCS)](https://cloud.google.com/storage)**: Used as the cloud storage solution for storing both raw and processed data, enabling efficient data access and analysis with other GCP tools.
- **[Terraform Infrastructure as Code (IaC)](https://www.terraform.io/)**: An open-source IaC tool employed to define and provision cloud infrastructure using code, automating the deployment of GCP resources for reproducible and scalable infrastructure.
- **[MageAI Workflow orchestration](https://www.mage.ai/)**: A data engineering platform that supports the creation and orchestration of data pipelines, managing workflows, scheduling jobs, and monitoring pipeline performance.
- **[dbt Data transformation](https://www.getdbt.com/)**: A data transformation tool that uses SQL to define transformations, streamlining the conversion of raw data into a more organized format and executing data quality checks.
- **[BigQuery Data warehouse](https://cloud.google.com/bigquery)**: A serverless data warehouse utilized for storing and analyzing large datasets, storing processed data, implementing data partitioning, and clustering.
- **[Looker Studio Dashboard](https://lookerstudio.google.com/)**: A data visualization tool that enables the creation of interactive dashboards and reports for visualizing data and sharing insights.
By leveraging these technologies, the project aims to establish a durable and scalable data pipeline capable of handling large data volumes and providing valuable insights into Citibike system usage patterns in NYC.
## **Data Pipeline**
The pipeline includes the following crucial components:
- Using the MageAI orchestrator, an ETL pipeline is implemented to fetch data from the API, remove duplicates, and extract data into the GCS bucket. Subsequently, the pipeline loads data from GCS and extracts it into the BigQuery data warehouse.
- dbt is used to carry out data transformation tasks, such as converting data types, adding a ride duration column, defining the ride time of day, merging Citibike rides data with station information, and adding a numeric station ID column from an external file. dbt's macros and seeds feature are utilized in data processing.
- The transformed data is partitioned and clustered in BigQuery to optimize query speed, with data partitioned by date and clustered by station ID.