import string
import random
import io
import pytest
import numpy as np

import validate_docstrings
validate_one = validate_docstrings.validate_one

from pandas.util.testing import capture_stderr


class GoodDocStrings(object):
    """
    Collection of good doc strings.

    This class contains a lot of docstrings that should pass the validation
    script without any errors.
    """

    def plot(self, kind, color='blue', **kwargs):
        """
        Generate a plot.

        Render the data in the Series as a matplotlib plot of the
        specified kind.

        Parameters
        ----------
        kind : str
            Kind of matplotlib plot.
        color : str, default 'blue'
            Color name or rgb code.
        **kwargs
            These parameters will be passed to the matplotlib plotting
            function.
        """
        pass

    def sample(self):
        """
        Generate and return a random number.

        The value is sampled from a continuous uniform distribution between
        0 and 1.

        Returns
        -------
        float
            Random number generated.
        """
        return random.random()

    def random_letters(self):
        """
        Generate and return a sequence of random letters.

        The length of the returned string is also random, and is also
        returned.

        Returns
        -------
        length : int
            Length of the returned string.
        letters : str
            String of random letters.
        """
        length = random.randint(1, 10)
        letters = "".join(random.sample(string.ascii_lowercase, length))
        return length, letters

    def sample_values(self):
        """
        Generate an infinite sequence of random numbers.

        The values are sampled from a continuous uniform distribution between
        0 and 1.

        Yields
        ------
        float
            Random number generated.
        """
        while True:
            yield random.random()

    def head(self):
        """
        Return the first 5 elements of the Series.

        This function is mainly useful to preview the values of the
        Series without displaying the whole of it.

        Returns
        -------
        Series
            Subset of the original series with the 5 first values.

        See Also
        --------
        Series.tail : Return the last 5 elements of the Series.
        Series.iloc : Return a slice of the elements in the Series,
            which can also be used to return the first or last n.
        """
        return self.iloc[:5]

    def head1(self, n=5):
        """
        Return the first elements of the Series.

        This function is mainly useful to preview the values of the
        Series without displaying the whole of it.

        Parameters
        ----------
        n : int
            Number of values to return.

        Returns
        -------
        Series
            Subset of the original series with the n first values.

        See Also
        --------
        tail : Return the last n elements of the Series.

        Examples
        --------
        >>> s = pd.Series(['Ant', 'Bear', 'Cow', 'Dog', 'Falcon'])
        >>> s.head()
        0   Ant
        1   Bear
        2   Cow
        3   Dog
        4   Falcon
        dtype: object

        With the `n` parameter, we can change the number of returned rows:

        >>> s.head(n=3)
        0   Ant
        1   Bear
        2   Cow
        dtype: object
        """
        return self.iloc[:n]

    def contains(self, pat, case=True, na=np.nan):
        """
        Return whether each value contains `pat`.

        In this case, we are illustrating how to use sections, even
        if the example is simple enough and does not require them.

        Parameters
        ----------
        pat : str
            Pattern to check for within each element.
        case : bool, default True
            Whether check should be done with case sensitivity.
        na : object, default np.nan
            Fill value for missing data.

        Examples
        --------
        >>> s = pd.Series(['Antelope', 'Lion', 'Zebra', np.nan])
        >>> s.str.contains(pat='a')
        0    False
        1    False
        2     True
        3      NaN
        dtype: object

        **Case sensitivity**

        With `case_sensitive` set to `False` we can match `a` with both
        `a` and `A`:

        >>> s.str.contains(pat='a', case=False)
        0     True
        1    False
        2     True
        3      NaN
        dtype: object

        **Missing values**

        We can fill missing values in the output using the `na` parameter:

        >>> s.str.contains(pat='a', na=False)
        0    False
        1    False
        2     True
        3    False
        dtype: bool
        """
        pass

    def mode(self, axis, numeric_only):
        """
        Ensure sphinx directives don't affect checks for trailing periods.

        Parameters
        ----------
        axis : str
            Sentence ending in period, followed by single directive.

            .. versionchanged:: 0.1.2

        numeric_only : bool
            Sentence ending in period, followed by multiple directives.

            .. versionadded:: 0.1.2
            .. deprecated:: 0.00.0
                A multiline description,
                which spans another line.
        """
        pass


class BadGenericDocStrings(object):
    """Everything here has a bad docstring
    """

    def func(self):

        """Some function.

        With several mistakes in the docstring.

        It has a blank like after the signature `def func():`.

        The text 'Some function' should go in the line after the
        opening quotes of the docstring, not in the same line.

        There is a blank line between the docstring and the first line
        of code `foo = 1`.

        The closing quotes should be in the next line, not in this one."""

        foo = 1
        bar = 2
        return foo + bar

    def astype(self, dtype):
        """
        Casts Series type.

        Verb in third-person of the present simple, should be infinitive.
        """
        pass

    def astype1(self, dtype):
        """
        Method to cast Series type.

        Does not start with verb.
        """
        pass

    def astype2(self, dtype):
        """
        Cast Series type

        Missing dot at the end.
        """
        pass

    def astype3(self, dtype):
        """
        Cast Series type from its current type to the new type defined in
        the parameter dtype.

        Summary is too verbose and doesn't fit in a single line.
        """
        pass

    def plot(self, kind, **kwargs):
        """
        Generate a plot.

        Render the data in the Series as a matplotlib plot of the
        specified kind.

        Note the blank line between the parameters title and the first
        parameter. Also, note that after the name of the parameter `kind`
        and before the colon, a space is missing.

        Also, note that the parameter descriptions do not start with a
        capital letter, and do not finish with a dot.

        Finally, the `**kwargs` parameter is missing.

        Parameters
        ----------

        kind: str
            kind of matplotlib plot
        """
        pass

    def method(self, foo=None, bar=None):
        """
        A sample DataFrame method.

        Do not import numpy and pandas.

        Try to use meaningful data, when it makes the example easier
        to understand.

        Try to avoid positional arguments like in `df.method(1)`. They
        can be alright if previously defined with a meaningful name,
        like in `present_value(interest_rate)`, but avoid them otherwise.

        When presenting the behavior with different parameters, do not place
        all the calls one next to the other. Instead, add a short sentence
        explaining what the example shows.

        Examples
        --------
        >>> import numpy as np
        >>> import pandas as pd
        >>> df = pd.DataFrame(np.ones((3, 3)),
        ...                   columns=('a', 'b', 'c'))
        >>> df.all(1)
        0    True
        1    True
        2    True
        dtype: bool
        >>> df.all(bool_only=True)
        Series([], dtype: bool)
        """
        pass


class BadSummaries(object):

    def wrong_line(self):
        """Exists on the wrong line"""
        pass

    def no_punctuation(self):
        """
        Has the right line but forgets punctuation
        """
        pass

    def no_capitalization(self):
        """
        provides a lowercase summary.
        """
        pass

    def no_infinitive(self):
        """
        Started with a verb that is not infinitive.
        """

    def multi_line(self):
        """
        Extends beyond one line
        which is not correct.
        """

    def two_paragraph_multi_line(self):
        """
        Extends beyond one line
        which is not correct.

        Extends beyond one line, which in itself is correct but the
        previous short summary should still be an issue.
        """


class BadParameters(object):
    """
    Everything here has a problem with its Parameters section.
    """

    def missing_params(self, kind, **kwargs):
        """
        Lacks kwargs in Parameters.

        Parameters
        ----------
        kind : str
            Foo bar baz.
        """

    def bad_colon_spacing(self, kind):
        """
        Has bad spacing in the type line.

        Parameters
        ----------
        kind: str
            Needs a space after kind.
        """

    def no_description_period(self, kind):
        """
        Forgets to add a period to the description.

        Parameters
        ----------
        kind : str
           Doesn't end with a dot
        """

    def no_description_period_with_directive(self, kind):
        """
        Forgets to add a period, and also includes a directive.

        Parameters
        ----------
        kind : str
           Doesn't end with a dot

           .. versionadded:: 0.00.0
        """

    def no_description_period_with_directives(self, kind):
        """
        Forgets to add a period, and also includes multiple directives.

        Parameters
        ----------
        kind : str
           Doesn't end with a dot

           .. versionchanged:: 0.00.0
           .. deprecated:: 0.00.0
        """

    def parameter_capitalization(self, kind):
        """
        Forgets to capitalize the description.

        Parameters
        ----------
        kind : str
           this is not capitalized.
        """

    def blank_lines(self, kind):
        """
        Adds a blank line after the section header.

        Parameters
        ----------

        kind : str
            Foo bar baz.
        """
        pass

    def integer_parameter(self, kind):
        """
        Uses integer instead of int.

        Parameters
        ----------
        kind : integer
            Foo bar baz.
        """
        pass

    def string_parameter(self, kind):
        """
        Uses string instead of str.

        Parameters
        ----------
        kind : string
            Foo bar baz.
        """
        pass

    def boolean_parameter(self, kind):
        """
        Uses boolean instead of bool.

        Parameters
        ----------
        kind : boolean
            Foo bar baz.
        """
        pass

    def list_incorrect_parameter_type(self, kind):
        """
        Uses list of boolean instead of list of bool.

        Parameters
        ----------
        kind : list of boolean, integer, float or string
            Foo bar baz.
        """
        pass


class BadReturns(object):

    def return_not_documented(self):
        """
        Lacks section for Returns
        """
        return "Hello world!"

    def yield_not_documented(self):
        """
        Lacks section for Yields
        """
        yield "Hello world!"

    def no_type(self):
        """
        Returns documented but without type.

        Returns
        -------
        Some value.
        """
        return "Hello world!"

    def no_description(self):
        """
        Provides type but no descrption.

        Returns
        -------
        str
        """
        return "Hello world!"

    def no_punctuation(self):
        """
        Provides type and description but no period.

        Returns
        -------
        str
           A nice greeting
        """
        return "Hello world!"


class TestValidator(object):

    def _import_path(self, klass=None, func=None):
        """
        Build the required import path for tests in this module.

        Parameters
        ----------
        klass : str
            Class name of object in module.
        func : str
            Function name of object in module.

        Returns
        -------
        str
            Import path of specified object in this module
        """
        base_path = "scripts.tests.test_validate_docstrings"

        if klass:
            base_path = ".".join([base_path, klass])

        if func:
            base_path = ".".join([base_path, func])

        return base_path

    @capture_stderr
    def test_good_class(self):
        errors = validate_one(self._import_path(
            klass='GoodDocStrings'))['errors']
        assert isinstance(errors, list)
        assert not errors

    @capture_stderr
    @pytest.mark.parametrize("func", [
        'plot', 'sample', 'random_letters', 'sample_values', 'head', 'head1',
        'contains', 'mode'])
    def test_good_functions(self, func):
        errors = validate_one(self._import_path(
            klass='GoodDocStrings', func=func))['errors']
        assert isinstance(errors, list)
        assert not errors

    @capture_stderr
    def test_bad_class(self):
        errors = validate_one(self._import_path(
            klass='BadGenericDocStrings'))['errors']
        assert isinstance(errors, list)
        assert errors

    @capture_stderr
    @pytest.mark.parametrize("func", [
        'func', 'astype', 'astype1', 'astype2', 'astype3', 'plot', 'method'])
    def test_bad_generic_functions(self, func):
        errors = validate_one(self._import_path(  # noqa:F821
            klass='BadGenericDocStrings', func=func))['errors']
        assert isinstance(errors, list)
        assert errors

    @pytest.mark.parametrize("klass,func,msgs", [
        # Summary tests
        ('BadSummaries', 'wrong_line',
         ('should start in the line immediately after the opening quotes',)),
        ('BadSummaries', 'no_punctuation',
         ('Summary does not end with a period',)),
        ('BadSummaries', 'no_capitalization',
         ('Summary does not start with a capital letter',)),
        ('BadSummaries', 'no_capitalization',
         ('Summary must start with infinitive verb',)),
        ('BadSummaries', 'multi_line',
         ('Summary should fit in a single line.',)),
        ('BadSummaries', 'two_paragraph_multi_line',
         ('Summary should fit in a single line.',)),
        # Parameters tests
        ('BadParameters', 'missing_params',
         ('Parameters {**kwargs} not documented',)),
        ('BadParameters', 'bad_colon_spacing',
         ('Parameters {kind} not documented',
          'Unknown parameters {kind: str}',
          'Parameter "kind: str" has no type')),
        ('BadParameters', 'no_description_period',
         ('Parameter "kind" description should finish with "."',)),
        ('BadParameters', 'no_description_period_with_directive',
         ('Parameter "kind" description should finish with "."',)),
        ('BadParameters', 'parameter_capitalization',
         ('Parameter "kind" description should start with a capital letter',)),
        ('BadParameters', 'integer_parameter',
         ('Parameter "kind" type should use "int" instead of "integer"',)),
        ('BadParameters', 'string_parameter',
         ('Parameter "kind" type should use "str" instead of "string"',)),
        ('BadParameters', 'boolean_parameter',
         ('Parameter "kind" type should use "bool" instead of "boolean"',)),
        ('BadParameters', 'list_incorrect_parameter_type',
         ('Parameter "kind" type should use "bool" instead of "boolean"',)),
        ('BadParameters', 'list_incorrect_parameter_type',
         ('Parameter "kind" type should use "int" instead of "integer"',)),
        ('BadParameters', 'list_incorrect_parameter_type',
         ('Parameter "kind" type should use "str" instead of "string"',)),
        pytest.param('BadParameters', 'blank_lines', ('No error yet?',),
                     marks=pytest.mark.xfail),
        # Returns tests
        ('BadReturns', 'return_not_documented', ('No Returns section found',)),
        ('BadReturns', 'yield_not_documented', ('No Yields section found',)),
        pytest.param('BadReturns', 'no_type', ('foo',),
                     marks=pytest.mark.xfail),
        pytest.param('BadReturns', 'no_description', ('foo',),
                     marks=pytest.mark.xfail),
        pytest.param('BadReturns', 'no_punctuation', ('foo',),
                     marks=pytest.mark.xfail)
    ])
    def test_bad_examples(self, capsys, klass, func, msgs):
        result = validate_one(self._import_path(klass=klass, func=func))  # noqa:F821
        for msg in msgs:
            assert msg in ' '.join(result['errors'])


class ApiItems(object):
    @property
    def api_doc(self):
        return io.StringIO('''
.. currentmodule:: itertools

Itertools
---------

Infinite
~~~~~~~~

.. autosummary::

    cycle
    count

Finite
~~~~~~

.. autosummary::

    chain

.. currentmodule:: random

Random
------

All
~~~

.. autosummary::

    seed
    randint
''')

    @pytest.mark.parametrize('idx,name', [(0, 'itertools.cycle'),
                                          (1, 'itertools.count'),
                                          (2, 'itertools.chain'),
                                          (3, 'random.seed'),
                                          (4, 'random.randint')])
    def test_item_name(self, idx, name):
        result = list(validate_docstrings.get_api_items(self.api_doc))
        assert result[idx][0] == name

    @pytest.mark.parametrize('idx,func', [(0, 'cycle'),
                                          (1, 'count'),
                                          (2, 'chain'),
                                          (3, 'seed'),
                                          (4, 'randint')])
    def test_item_function(self, idx, func):
        result = list(validate_docstrings.get_api_items(self.api_doc))
        assert callable(result[idx][1])
        assert result[idx][1].__name__ == func

    @pytest.mark.parametrize('idx,section', [(0, 'Itertools'),
                                             (1, 'Itertools'),
                                             (2, 'Itertools'),
                                             (3, 'Random'),
                                             (4, 'Random')])
    def test_item_section(self, idx, section):
        result = list(validate_docstrings.get_api_items(self.api_doc))
        assert result[idx][2] == section

    @pytest.mark.parametrize('idx,subsection', [(0, 'Infinite'),
                                                (1, 'Infinite'),
                                                (2, 'Finite'),
                                                (3, 'All'),
                                                (4, 'All')])
    def test_item_subsection(self, idx, subsection):
        result = list(validate_docstrings.get_api_items(self.api_doc))
        assert result[idx][3] == subsection
