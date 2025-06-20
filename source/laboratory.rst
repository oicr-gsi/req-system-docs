##################
Laboratory Users
##################

This role includes both TGL staff as well as the Cancer Genomics Interpreter (CGI) team. CGI prepares draft clinical and QC reports and uploads PDF documents for review by Sign Out users. This team aggregates pipeline outputs to create a draft genomic report.  This protocol is limited to uploading the draft clinical and QC report to a respective requisition via the OICR Genomics Requisition System for review by licensed Geneticists only. 

.. _upload-draft:

Uploading a Draft Clinical Report
=====================================

#. From your account dashboard, navigate to the submissions tab and select the study. 
#. Select the requisition ID by marking the record, and under the “Actions” column, select “Edit Submission”. 
#. Scroll to the requisition header “Data Report”.  Upload the draft clinical report PDF (no PHI) under Data report>Genomic report (PDF).  Upload the QC Report under Data report>QC report (PDF). Select “Data is ready for review” and click submit. The draft report can no longer be edited by a Laboratory user until Geneticist (Sign Out user) review.
#. The requisition status will display “Draft Report Ready for Review”. The Sign Out user will receive an email and will be able to review the draft report.

Re-Opening (Revising) a Rejected Draft Clinical Report
==========================================================

A Geneticist (Sign Out user) may reject a draft clinical report.  The CGI team is responsible for addressing and seeking a resolution under direction from the Geneticist. 

#. A notification email will be received with details of the rejected draft report.
#. From the study requisition dashboard, select the case with status “Draft Report Not Accepted”.
#. From the requisition case history, review the Geneticist’s comments and seek resolution, see below.  If further discussion is required, contact the responsible Geneticist.  Revise the draft genomic report. 
#. From the case history tab, select edit, or from the study requisition dashboard, select the requisition and under “Actions” select “Edit Submission”.  
#. Scroll to the bottom of the requisition and select “Reopen submission”.  A text box will appear.  Provide a justification for reopening and editing the draft genomic report. Click “Submit”.
#. The requisition status will change to “Submission Approved”.  A notification email will be sent to the Sign Out user , alerting Geneticists that a revised clinical report is anticipated. The data report PDF fields will now permit upload of a new genomic report and/or QC report.  
#. To remove the existing erroneous draft genome report or QC report, click “Remove”.  
#. Upload the corrected and versioned draft genomic report and/or QC PDF report, select “Data is ready for review” and click “submit”.  The draft report can no longer be edited by a Laboratory user. Note, prior draft reports may be reviewed in the requisition case history.
#. The requisition status will display “Draft Report Ready for Review”. The Sign Out user will receive an email and will review the revised draft report.

Reviewing a Requisitioner-Edited Submission to “Non-PHI” or “PHI & Non-PHI”
============================================================================

A Requisitioner may edit a requisition at any time, including after case sign out. When these events occur, Laboratory users are notified by email.  The dashboard status of requisitions will revert to “Submitted” and the changes will first need to be accepted by the Accessioner. The requisition case history documents all versions of a requisition, including change request comments. Updates to LIMS, Revised QC and/or genomic reports may be required.   

If materials have been received at OICR, and transferred to the Translational Genomics Laboratory, the following steps must be followed by Laboratory roles (MLTs and CGI).


Prior to Sign Out (Laboratory-MLTs)
------------------------------------

#. Navigate to the Submissions tab and select the study specific requisition ID that was edited by the Requisitioner as noted in the notification email. 
#. If the requisition status is “Submitted”, the Accessioner has not reviewed the changes to the requisition and updates to MISO LIMS records have not occurred. The requisition may not be visible to Laboratory users. Do not proceed until status changes to “Submission Approved”. 
#. If the requisition status is “Submission approved”, MLTs must review the changes to materials associated with the requisition ID within MISO LIMS for associated sample aliquots, libraries, or library aliquot change logs; update any affected material labels.  

Reviewing a Requisitioner-Edited Submission (Laboratory-CGI)
------------------------------------------------------------

#. Navigate to the Submissions tab and select the study specific requisition ID that was edited by the Requisitioner as noted in the notification email
#. If the requisition status is “Submitted”, the Accessioner has not approved the changes to the requisition and updates to MISO LIMS records have not occurred. The requisition may not be visible to Laboratory users. Wait until status is “Submission approved” before proceeding. 
#. If the requisition status is “Submission approved”, CGI must review the changes to the requisition for non-PHI field changes that are not captured within MISO LIMS that may alter the draft genomic report and/or QC report. Verify requisition date and time stamps to ensure you are reviewing the updated requisition.
#. If necessary, revise the draft genomic and QC report with changed information following procedures as outlined in :ref:`upload-draft`. 


Consent Withdrawal 
===================

#. Consent withdrawal will appear within the requisition case history and may be quickly identified on study dashboards under “Consent withdrawn”. The requisition status will display “Withdraw Consent”.
#. The record must be marked in MISO as “Consent Withdrawn” and no further processing/analysis is permitted.  


Modifying the requisitioned assay
=================================

This option is only available when the submission is in “Submission Approved” or “Draft Report Ready for Review” statuses.

#. In the drop-down menu on the Submission tab, click “Edit Submission”
#. In the “Accredited Assay Selection” section, select the new assay. Click “Save”.

An email will be sent out to all interested parties and the submission will be returned to “Submitted” status, requiring an Accessioner to approve it again.

.. toctree::
   :maxdepth: 2