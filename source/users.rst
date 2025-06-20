##############
User Accounts
##############

The OICR Genomics Requisition System user accounts, study and access permissions and site-specific study requisition forms are granted/created upon study approval. 

.. _request-user:

Requesting a User Account/Access Change Request
================================================

The Administrator must receive a completed TW-024 OICR Genomics Requisition System Access Request Form from the academic study sponsor, site co-investigator, or their authorized delegate for each authorized account, specifying the user role (Requisitioner or Sign Out) as defined in :ref:`user-roles`. The study sponsor or delegate must also immediately submit a TW-024 OICR Genomics Requisition System Access Request Form for any employee whose employment status or study assignment has changed. All accounts require an institutional email address. 

Account Creation, Password Configuration and Account Agreement Terms
====================================================================

Since the introduction of multi-factor authentication (MFA), this process has changed. 

#. The Administrator will add users to a specific study site requisition form following :ref:`configure-study-roles`.
#. The Administrator submits a ticket to OICR IT (helpdesk@oicr.on.ca) requesting the user’s password be set to permit MFA. Include the user’s name and email address, and the system (Genomics Requisition and Reporting system).
#. The user will receive an email notification “Genomics Requisition Forms-Account Created”. Ensure they add requisition.genomics@oicr.on.ca to their email account safe senders list. This email notifies the user that their password will arrive shortly from OICR’s IT team.
#. OICR IT will create the user account in Crowd and email a password to the user.
#. Upon first login, the user will be prompted to accept the new account agreement.
#. After accepting the account agreement, the user must complete their basic profile information.
#. The user can then use the Account Settings page to set their password to something more memorable.

Password Reset
===============

If you have access to the system and wish to reset your password, follow these steps: 

#. From the OICR Genomics Requisition System, select Login, and select “Forgot your password”. 
#. Enter your account email address.
#. The portal will display the following notification and the user will receive an email notification with subject header “OICR Genomics Requisition Forms- Reset Your Password”.
#. From the notification email, select “Reset your password”.
#. Set a new password.

If you have forgotten your password, please email helpdesk@oicr.on.ca and request your password for the OICR Genomics Requisition System be reset.

User Account and Password Expiry Policies
===========================================

Accounts that are not accessed for a period >1 year will automatically be deactivated.  If your account is deactivated, please contact the Administrator.  

Passwords must be reset every year.  Users will be prompted to select a new password 1 year from initial account activation.



.. _user-roles:

##############
User Roles
##############

There are two categories of user roles: global user roles and study specific user roles. A specific user can have from none to all of these user roles.

Study Roles
=============

Study specific user roles are assigned per form, granting specific permissions to that form alone. These roles ensure tracking of all stages of a requisition lifecycle from sample submission to report generation and sign out. 

Key activities of each role are defined below. 

#. :doc:`Requisitioner <requisitioners>` (full PHI access): Includes external Clinical Coordinators, who are authorized to view PHI and patient information. Requisitioners may:

   * Submit a requisition
   * Withdraw a requisition (user entry error)
   * Edit a requisition
   * Submit notification of consent withdrawal
   * Print requisition for inclusion in medical record (includes PHI) 
   * Print shipping manifest (no PHI)
   * Rescind signed out clinical reports to correct PHI and/or non-PHI fields

#. :doc:`Accessioner <accessioners>` (no PHI access): Includes Tissue Portal staff, who may:

   * Approve a requisition/requisition edit (non-PHI fields)
   * Accept a shipment following receipt at OICR
   * Download MISO LIMS information
   * Review rescinded requisitions and genomic reports for required changes to non-PHI fields (Requisitioner initiated)
   * Report privacy breaches 

#. :doc:`Laboratory <laboratory>` (no PHI access): Includes Cancer Genomics Interpreter (CGI) informatics staff and Medical Laboratory Technicians (MLTs), who may:

   * Upload a draft clinical report (no PHI), triggering an email notification to a Sign Out user
   * Reopen and upload a revised draft clinical report (no PHI), triggering an email notification to a Sign Out user
   * Review requisition edits (non-PHI fields)
   * Review rescinded requisitions and genomic reports for required changes to non-PHI fields (Requisitioner initiated)

#. :doc:`Sign Out <signout>` (full PHI access): Includes external Geneticists (ACMG/CCMG) who are authorized to view PHI and patient information. Sign Out users may:

   * Review and approve or reject a draft clinical report
   * Review requisition edits (PHI and non-PHI fields)
   * Approve or reject revisions to rescinded clinical reports

#. :doc:`Administrator <study-admins>` (no PHI access): Includes the Genomics Program Manager and GSI Director, who may:

   * Create and customize specific study requisition form templates
   * Add/remove user access and assign study specific user roles
   * Monitor de-identified sample withdrawals, consent withdrawals, rejected clinical reports, rescinded clinical reports, report progress, and system auditing


Global Roles
============

Global user roles control the Requisition System, permitting users to modify system level pages, emails, and forms. These roles are visible from My Account > Account Settings, in the User Settings area. 

There are three global user roles:

* :ref:`global-admins` (no PHI access): Includes the GSI Director and individuals in IT

   * Assign other users global roles
   * Modify pages on the requisition other than forms 

* :ref:`form-admins` (no PHI access): Includes the Genomics Program Manager and GSI Director, who may:

   * Create and customize specific study requisition form templates
   * Add/remove user access and assign study specific user roles
   * Monitor de-identified sample withdrawals, consent withdrawals, rejected clinical reports, rescinded clinical reports, report progress, and system auditing.
   * Clone existing requisitions after software revision
   * Merge requisition forms
   * Commit forms metadata to GitHub

* No role (no PHI access): the default level for all users not granted one of the two other roles.

Every user has no role until they are granted one by a global Administrator.


####################
Notification Emails
####################

Study roles may receive a number of notifications by email. Their subjects, targets, and next steps are detailed below.

+--------------------------+-----------------+---------------------------------------+
| Email Subject            | Who is notified |  Next Steps                           |
+==========================+=================+=======================================+
| Submitted                |   accessioner,  |  :ref:`approve-submission`            |
|                          |   admin         |                                       |
+--------------------------+-----------------+---------------------------------------+
| Requisition received     |   requisitioner |  Wait for approval                    |
+--------------------------+-----------------+---------------------------------------+
| Approval required        |   accessioner,  |   :ref:`approve-edited-submission`    |
|                          |   laboratory    |                                       |
+--------------------------+-----------------+---------------------------------------+
| Withdrawn                | requisitioner,  |                                       |
|                          | accessioner,    |   Accessioner: :ref:`acc-withdraw`    |
|                          | admin           |                                       |
+--------------------------+-----------------+---------------------------------------+
| Approved to ship samples |   requisitioner |   :ref:`ship-materials`               |  
+--------------------------+-----------------+---------------------------------------+
| Incoming shipment        |   accessioner   |   Informational                       |
+--------------------------+-----------------+---------------------------------------+
| Denied                   |   requisitioner |   :ref:`denied-submission`            |
+--------------------------+-----------------+---------------------------------------+
| Consent withdrawn        |   requisitioner,|  Requisitioner, Admin: informational; |
|                          |   accessioner,  |  Accessioner: :ref:`acc-consent`;     |
|                          |   admin,        |  Laboratory: :ref:`lab-consent`;      |
|                          |   laboratory,   |  Sign-out: :ref:`sign-consent`;       |
|                          |   signout       |                                       |
+--------------------------+-----------------+---------------------------------------+
| Draft ready for review   |   signout       |  :ref:`review-draft`                  |
+--------------------------+-----------------+---------------------------------------+
| Signed out               |   requisitioner,|   Requisitioner: :ref:`req-signedout` |
|                          |   accessioner,  |                                       |
|                          |   admin,        |                                       |
|                          |   laboratory    |                                       |
+--------------------------+-----------------+---------------------------------------+
| Rescinded  (Non-PHI)     |   laboratory,   |   :ref:`lab-rescinded`                |
|                          |   admin         |                                       |
+--------------------------+-----------------+---------------------------------------+
| Rescinded (PHI and       |   laboratory,   |   :ref:`lab-rescinded`                |
| non-PHI)                 |   admin         |                                       |
+--------------------------+-----------------+---------------------------------------+
| Rescinded (PHI only)     |   admin         |   Informational                       |
+--------------------------+-----------------+---------------------------------------+
| PHI updated              |   admin,        |   :ref:`sign-phi-change`              |
|                          |   signout       |                                       |
+--------------------------+-----------------+---------------------------------------+
| PHI updates rejected     |   requisitioner |   :ref:`phi-reject`                   |
+--------------------------+-----------------+---------------------------------------+
| Draft not accepted       |   laboratory    |   :ref:`draft-reopen`                 |
+--------------------------+-----------------+---------------------------------------+
| Draft re-opened          |   laboratory    |   Informational                       |
+--------------------------+-----------------+---------------------------------------+


.. toctree::
   :maxdepth: 2
