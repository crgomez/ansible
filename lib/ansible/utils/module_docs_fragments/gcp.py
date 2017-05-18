# (c) 2017, Carlos Gomez, Tom Melendez <crgomez@google.com, supertom@google.com>
#
# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.

class ModuleDocFragment(object):

   #GCP only documentation fragment.
   DOCUMENTATION
  
options:
  add_project:
    description:
        -You will need to create a Google Cloud Platform Project as a first step.
         Make sure you are logged in to your Google Account (gmail, Google+, etc). 
    required: true
    default: null
      
  project_id:
    description:
        -In order for ansible to create Compute Engine instances, you'll need a
         Service Account. It's recommended that you create a new Service Account
         (don't use the default)
    required: true
    default: null
    scopes: null
    iam_role: null
    
  requirments:
  -"python >= 2.7"
  -"google cloud platform"
  -"google cloud sdk"
 #Notes:
 #
