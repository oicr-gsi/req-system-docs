## Syntax Notes
| Table | Table | Table | Table |
| ----------- | ----------- | ----------- | ----------- |
| Header | <ul><li>(1)</li><li>(2)</li><li>(3)</li><li>(4)</li><li>(4)</li><li>(5)</li><li>(6)</li></ul> | Item | Item |
| **Paragraph** | <ul><li>(1)</li></ul> | Item | Item |
| **Paragraph** | <ul><li>(1)</li><li>(2)</li></ul> | Item | Item |
| **Paragraph** | <ul><li>(1)</li><li>(2)</li><li>(3)</li></ul> | Item | Item |
| **Paragraph** | <ul><li>(1)</li><li>(2)</li><li>(3)</li><li>(4)</li></ul> | Item | Item |
| **Paragraph** | <ul><li>(1)</li><li>(2)</li><li>(3)</li><li>(4)</li><li>(5)</li></ul> | Item | Item |
| **Paragraph** | <ul><li>(1)</li><li>(2)</li><li>(3)</li><li>(4)</li><li>(5)</li><li>(6)</li></ul> | Item | Item |






# REDCap Requisition System for OICR
### Using REDCap's Database and Data Collection Functionality to Create an Updated Requisition System
## Table of Contents
1. Users and Permissions
2. Statuses and Conditions
3. Instruments
4. Data Access Groups
5. Data Collection Flow (intended)
6. Glossary
7. Item
8. Item
9. Item
10. Item 

## Users and Permissions
1. **Requisitioner:** External Collaborator clinician or clinical coordinator who submits requisitions and retrieves final reports, **access to PHI**
2. **Accessioner:** Internal Accessioning Staff; OICR Tissue Portal, who reviews requisitions, enters them into MISO, and receives tissue shipments, **no access to PHI**
3. **Laboratory:** Internal Staff OICR Genomics, who monitor and administrate requisitions, submit draft reports, **no access to PHI** (Note; several iterations of a draft report might be necessary before the Geneticist is satisfied)
4. **Sign-out:** Geneticist; the clinical geneticist who reviews draft reports, edits them with PHI, and signs out the final reports, **access to PHI**
5. **Administrator:** Internal QA Staff; review submissions, ensure that items are moving as intended, may have PHI access.  Reports issues to Form Administrator
6. **Form Administrator:** Internal Infrastructure Staff, manages creation and upkeep of REDCap project environment. Resolves technical issues raised by Form Administrator.  No access to PHI.
7. **Super Administrator:** Internal IT Staff, highest level of technical clearance.  Manages server and security issues with the entire REDCap instance.  **access to PHI**

## Statuses and Conditions
| REDCap Status | Procedure | Requisition Status | Conditions |
| ----------- | ----------- | ----------- | ----------- |
| **Not Submitted** | <ul><li>(1)A requisitioner begins the submission and submits Requisition Status, but does not complete either Patient Information or Specimen Information</li></ul> | <ul><li>(1) Note Submitted</li></ul> | <ul><li>(1) Patient Info, Specimen info not complete</li></ul> |
| **Waiting Accessioner Approval** | <ul><li>(1) A requisitioner completes Requisition Status, Patient Information, and Specimen Information</li></ul> | <ul><li>(1) Open</li></ul> | <ul><li>(1) Patient Info, Specimen info complete</li></ul> |
| **Approved** | <ul><li>(1) A requisitioner completes Requisition Status, Patient Information, and Specimen Information</li><li>(2) An accessioner reviews the information on Requisition Status and selects 'Approve'</li></ul> | Item | Item |

## Instruments

### Instrument List
1. Record
2. Status
3. Assay
4. Requistion
5. Draft Report
6. Final Report
7. Manifest
8. Requisition Calculated Fields (Invisible Instrument for Form Administrator Purposes)

### Instrument Interaction Structure

## Data Access Groups (DAGs)

## 
