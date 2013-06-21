from django.core.urlresolvers import reverse
from django.test.utils import override_settings

from xmodule.modulestore.tests.factories import CourseFactory, ItemFactory

from xmodule.modulestore.tests.django_utils import ModuleStoreTestCase

import xmodule.modulestore.django

from helpers import LoginEnrollmentTestCase, check_for_get_code
from modulestore_config import TEST_DATA_MONGO_MODULESTORE


@override_settings(MODULESTORE=TEST_DATA_MONGO_MODULESTORE)
class TestNavigation(ModuleStoreTestCase, LoginEnrollmentTestCase):

    STUDENT_INFO = [('view@test.com', 'foo'), ('view2@test.com', 'foo')]

    """
    Check that navigation state is saved properly.
    """

    def setUp(self):
        xmodule.modulestore.django._MODULESTORES = {}

        self.course = CourseFactory.create()
        self.full = CourseFactory.create(display_name='Robot_Sub_Course')
        self.chapter0 = ItemFactory.create(parent_location=self.course.location,
                                           display_name='Overview')
        self.chapter9 = ItemFactory.create(parent_location=self.course.location,
                                           display_name='factory_chapter')
        self.section0 = ItemFactory.create(parent_location=self.chapter0.location,
                                           display_name='Welcome')
        self.section9 = ItemFactory.create(parent_location=self.chapter9.location,
                                           display_name='factory_section')

        # Create student accounts and activate them.
        for i in range(len(self.STUDENT_INFO)):
            self.create_account('u{0}'.format(i), self.STUDENT_INFO[i][0], self.STUDENT_INFO[i][1])
            self.activate_user(self.STUDENT_INFO[i][0])

    def test_redirects_first_time(self):
        """
        Verify that the first time we click on the courseware tab we are
        redirected to the 'Welcome' section.
        """
        self.login(self.STUDENT_INFO[0][0], self.STUDENT_INFO[0][1])
        self.enroll(self.course, True)
        self.enroll(self.full, True)

        resp = self.client.get(reverse('courseware',
                               kwargs={'course_id': self.course.id}))

        self.assertRedirects(resp, reverse(
            'courseware_section', kwargs={'course_id': self.course.id,
                                          'chapter': 'Overview',
                                          'section': 'Welcome'}))

    def test_redirects_second_time(self):
        """
        Verify the accordion remembers we've already visited the Welcome section
        and redirects correpondingly.
        """
        self.login(self.STUDENT_INFO[0][0], self.STUDENT_INFO[0][1])
        self.enroll(self.course, True)
        self.enroll(self.full, True)

        self.client.get(reverse('courseware_section', kwargs={'course_id': self.course.id,
                                                              'chapter': 'Overview',
                                                              'section': 'Welcome'}))

        resp = self.client.get(reverse('courseware',
                               kwargs={'course_id': self.course.id}))

        self.assertRedirects(resp, reverse('courseware_chapter',
                                           kwargs={'course_id': self.course.id,
                                                   'chapter': 'Overview'}))

    def test_accordion_state(self):
        """
        Verify the accordion remembers which chapter you were last viewing.
        """

        self.login(self.STUDENT_INFO[0][0], self.STUDENT_INFO[0][1])
        self.enroll(self.course, True)
        self.enroll(self.full, True)

        # Now we directly navigate to a section in a chapter other than 'Overview'.
        check_for_get_code(self, 200, reverse('courseware_section',
                                              kwargs={'course_id': self.course.id,
                                                      'chapter': 'factory_chapter',
                                                      'section': 'factory_section'}))

        # And now hitting the courseware tab should redirect to 'factory_chapter'
        resp = self.client.get(reverse('courseware',
                               kwargs={'course_id': self.course.id}))

        self.assertRedirects(resp, reverse('courseware_chapter',
                                           kwargs={'course_id': self.course.id,
                                                   'chapter': 'factory_chapter'}))