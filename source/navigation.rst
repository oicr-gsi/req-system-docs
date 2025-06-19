################################################
Navigation
################################################

All users begin their session at OICR Genomics Requisition System landing page.  Permissions for each study are granted by the Administrator. Clinical Program managers may be granted access to more than one study as required to monitor their team’s respective activities.  

Dashboard
==========

Upon user login, users are directed to their dashboard as seen above.  Each menu tab contains the following information:

* Dashboard: All recent activity including submitted requisitions and associated identities (IDs).
* My Account (My Profile): User account information.
* Submissions
* Manage Forms : Visible to Administrators and Form Administrators

My Account
==========

My Account displays a drop-down contains information about the current user.

* My Profile: Modify the user’s first and last name. After making any changes, press ‘Save Changes’.
* Account Settings: View email address, update password, view global roles, status of the account, selected language, and timezone. After making any changes, press ‘Save Changes’.

Submissions
===========

The Submissions tab has a drop-down list of the submitted forms from every requisition form the current user is permitted to view. If a user’s role does not permit them access to submissions, there may be no drop-down visible.

Once a user selects a requisition form from the Submission drop-down, they will see the Study Submissions page.

Summary section
---------------

The summary section is an aggregate view of all requisition status states. Note, status state icons will only appear in the “Summary” field after a requisition has reached this status state at least once for a given study form. For a complete list of possible statuses, see Requisition Lifecycle. 

Table with submissions
----------------------

The submissions table contains the status of all study requisitions the user can view. 

* Filter section: filter the requisitions by status, updated date, and keywords
* Bulk Actions: select submissions with the check boxes at the left and use the drop-down to perform a bulk action on all requisitions simultaneously
* Table columns

	* ID: the unique requisition ID. Clicking on the ID of any submission will take the user to the submitted form for review.
	* Submitted by: the name and email address of the requisitioner who submitted the form.
	* Created Date: the date the requisition was submitted
	* Status (Last Change Date): the status of the requisition and date last modified. See “Requisition Lifecycle” for a complete list of statuses.
	* Actions: select the drop-down to perform an action on the requisition appropriate for its status and role.


Requisition Page
----------------

The requisition page, accessed through the Study Submissions page, has the full contents of the requisition forms that the user is permitted to view (e.g. a Laboratory User cannot view submissions that are not approved, nor can they view PHI).

On the left side is a listing of all requisition forms for this study, including the status, last modified date, and Action drop-down from the Study Submissions page. The same set of actions is available at the top right for the form currently in view. 

In the center is a specific requisition. The unique requisition ID is at the top, as well as the status, last modified date, and requisitioner. 

The submission tab shows the contents of the form as it was submitted. If permitted by role and status, modifications are also made here, including uploading QC and clinical reports.


Requisition Case History
------------------------

The case history contains a date and time stamped audit log of all requisition status changes as performed by all users. All requisition status changes, Accessioner submission denials and rejected draft genomic report notes may be reviewed from the “Case History” tab

#. Select a requisition ID from the study dashboard as seen below.  
#. Select the “Case History” tab, as seen below. 


Manage Forms
=============

The “Manage Forms” dashboard contains form management configuration options and is available to Administrators of specific forms as well as global Form Administrators. 


.. toctree::
   :maxdepth: 2

