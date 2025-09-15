#################
Accessioners
#################

After a Requisitioner submits a new requisition, or after they have edited a requisition, the requisition must be approved by an OICR Accessioner.  An OICR Accessioner may be responsible for approving requisitions from several study specific requisitions and requisition user accounts.  OICR Accessioners are assigned to each study specific requisition and multiple Accessioners may be responsible for one or more studies.  If you are designated an Accessioner, you will receive an email notification of a new requisition with ID and instructions indicating next actions that are required upon logging into the OICR Genomics Requisition System.  Please note, samples should not ship prior to acceptance of a requisition.

.. _approve-submission:

Approving a Submission
======================

#. When a Requisitioner submits a new requisition, the OICR Accessioner will receive a notification email .  This email will identify the requisition ID and user account submitting the requisition.  The Accessioner may click on the login link embedded within the email or login directly to the OICR Genomics Requisition System to approve the submission.
#. Log in to the OICR Genomics Requisition System. Navigate to the Submissions tab and select the study specific requisition.  From the study dashboard, select the requisition that is pending approval by clicking on the requisition ID and review the submission for accuracy; ensure study IDs match the study specific requisition.

	#. The requisition may be approved directly from the Study Submisson page by selecting “Approve” in the actions column. 
	#. Alternatively, the requisition may be approved directly from the requisition form after review by selecting “Approve” from the drop-down menu in the right-hand margin of the requisition. 

#. After selecting “Approve” for a requisition, the Approval dialogue box will appear.  The Accessioner may add a comment if desired.  This comment will be visible to all users in the requisition case history. Select “Approve”.
#. The Accessioner will receive an email indicating that a shipment will be incoming. 

.. _approve-edited-submission:

Approving a Requisitioner Edited Submission
===========================================

A Requisitioner may edit a requisition at any time, even after sign out. When non-PHI fields are edited, Accessioners are notified by email.  If the Requisitioner edits the requisition prior to Accessioner approval and material shipment, the requisition record will reflect the most recent version. All requisition versions may be reviewed in the requisition case history. 

If materials have been received at OICR, the following procedure must be followed.

The status of the submission will be “Submitted”. 

#. Within the requisition, select the case history. 
#. Review changes to the requisition by comparing requisition fields between the original submission and the revised submission and/or case history comment fields. Both the original and the revised requisition are available in the case history.
#. Verify requisition date and time stamps to ensure you are reviewing the edited requisition.
#. If non-PHI field changes are acceptable, approve the requisition as documented in :ref:`approve-submission`.  Note, changes may have occurred within PHI fields that are not visible to the Accessioner (your) role. 
#. The Accessioner will receive an email notification about an incoming shipment.  This notification may be disregarded.
#. If materials were previously received at OICR and accessioned into MISO LIMS but have not yet been transferred outside of OICR Tissue Portal, make required changes to LIMS identities and/or material labels. 
#. If materials (nucleic acid aliquots) have been transferred to the Translational Genomics Laboratory (TGL), and changes are required to LIMS identities, notify TGL staff. They will update their LIMS entries and/or update material labels. 

.. _reject-submission:

Rejecting a Submission 
======================

#. In practice, Accessioners work with the Requisitioners to resolve issues rather than rejecting a submission. The instructions for rejecting a submission are included here for extraordinary cases. From the user dashboard, navigate to the “Submissions” tab and select the study specific requisition.  
#. From the study submissions dashboard, select “Deny” from the “Actions” column. Alternatively, the requisition may be denied directly from the drop-down menu at the top of the requisition. 
#. Upon selection of “Deny”, a dialog box will appear.  Within this dialog box, provide a justification for denial of the requisition by selecting “Add Comment”. Click “Deny”.  This information will appear in the case history of the requisition. 
#. The case status will appear as “Submission denied”. 

.. _acc-withdraw:

Withdrawing a Study Specific Requisition 
=========================================

A Requisitioner may accidentally submit a requisition in error.  Should a Requisitioner catch this error, they may withdraw the sample before receipt at OICR.  This situation could occur after shipment and/or receipt at OICR. If this situation occurs, the Accessioner will receive an email notification.

.. _acc-consent:

Consent Withdrawal 
===================

Consent withdrawal is initiated by the Requisitioner role, however the Accessioner role must immediately flag the associated MISO identity within OICR’s LIMS system.

#. When consent is withdrawn, a notification email will be received by all roles.  Consent withdrawal will appear within the requisition case history and may be quickly identified on study dashboards under “Consent Withdrawn”. 
#. Within MISO LIMS, search for the respective requisition ID.  Edit the identity under Identity>Consent>, mark record as “Revoked”.

Accessioners must retrieve all samples and derivatives from all associated workgroups and move materials to respective “consent withdrawn” locations in -20°C or -80°C located within Tissue Portal.  Samples and derivatives may require destruction and/or return to external site. 


.. toctree::
   :maxdepth: 2 


+----------------+----------------------+
| **Change Log** | `Github commit log`_ |
+----------------+----------------------+

.. _Github commit log : https://github.com/oicr-gsi/req-system-docs/commits/main/source/accessioners.rst
