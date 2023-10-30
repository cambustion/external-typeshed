"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
Protocol messages for describing input data Examples for machine learning
model training or inference.
"""
import builtins
import sys

import google.protobuf.descriptor
import google.protobuf.message
import tensorflow.core.example.feature_pb2

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class Example(google.protobuf.message.Message):
    """An Example is a mostly-normalized data format for storing data for
    training and inference.  It contains a key-value store (features); where
    each key (string) maps to a Feature message (which is oneof packed BytesList,
    FloatList, or Int64List).  This flexible and compact format allows the
    storage of large amounts of typed data, but requires that the data shape
    and use be determined by the configuration files and parsers that are used to
    read and write this format.  That is, the Example is mostly *not* a
    self-describing format.  In TensorFlow, Examples are read in row-major
    format, so any configuration that describes data with rank-2 or above
    should keep this in mind. If you flatten a matrix into a FloatList it should
    be stored as [ row 0 ... row 1 ... row M-1 ]

    An Example for a movie recommendation application:
      features {
        feature {
          key: "age"
          value { float_list {
            value: 29.0
          }}
        }
        feature {
          key: "movie"
          value { bytes_list {
            value: "The Shawshank Redemption"
            value: "Fight Club"
          }}
        }
        feature {
          key: "movie_ratings"
          value { float_list {
            value: 9.0
            value: 9.7
          }}
        }
        feature {
          key: "suggestion"
          value { bytes_list {
            value: "Inception"
          }}
        }
        # Note that this feature exists to be used as a label in training.
        # E.g., if training a logistic regression model to predict purchase
        # probability in our learning tool we would set the label feature to
        # "suggestion_purchased".
        feature {
          key: "suggestion_purchased"
          value { float_list {
            value: 1.0
          }}
        }
        # Similar to "suggestion_purchased" above this feature exists to be used
        # as a label in training.
        # E.g., if training a linear regression model to predict purchase
        # price in our learning tool we would set the label feature to
        # "purchase_price".
        feature {
          key: "purchase_price"
          value { float_list {
            value: 9.99
          }}
        }
     }

    A conformant Example data set obeys the following conventions:
      - If a Feature K exists in one example with data type T, it must be of
          type T in all other examples when present. It may be omitted.
      - The number of instances of Feature K list data may vary across examples,
          depending on the requirements of the model.
      - If a Feature K doesn't exist in an example, a K-specific default will be
          used, if configured.
      - If a Feature K exists in an example but contains no items, the intent
          is considered to be an empty tensor and no default will be used.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FEATURES_FIELD_NUMBER: builtins.int
    @property
    def features(self) -> tensorflow.core.example.feature_pb2.Features: ...
    def __init__(
        self,
        *,
        features: tensorflow.core.example.feature_pb2.Features | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["features", b"features"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["features", b"features"]) -> None: ...

global___Example = Example

@typing_extensions.final
class SequenceExample(google.protobuf.message.Message):
    """A SequenceExample is an Example representing one or more sequences, and
    some context.  The context contains features which apply to the entire
    example. The feature_lists contain a key, value map where each key is
    associated with a repeated set of Features (a FeatureList).
    A FeatureList thus represents the values of a feature identified by its key
    over time / frames.

    Below is a SequenceExample for a movie recommendation application recording a
    sequence of ratings by a user. The time-independent features ("locale",
    "age", "favorites") describing the user are part of the context. The sequence
    of movies the user rated are part of the feature_lists. For each movie in the
    sequence we have information on its name and actors and the user's rating.
    This information is recorded in three separate feature_list(s).
    In the example below there are only two movies. All three feature_list(s),
    namely "movie_ratings", "movie_names", and "actors" have a feature value for
    both movies. Note, that "actors" is itself a bytes_list with multiple
    strings per movie.

    context: {
      feature: {
        key  : "locale"
        value: {
          bytes_list: {
            value: [ "pt_BR" ]
          }
        }
      }
      feature: {
        key  : "age"
        value: {
          float_list: {
            value: [ 19.0 ]
          }
        }
      }
      feature: {
        key  : "favorites"
        value: {
          bytes_list: {
            value: [ "Majesty Rose", "Savannah Outen", "One Direction" ]
          }
        }
      }
    }
    feature_lists: {
      feature_list: {
        key  : "movie_ratings"
        value: {
          feature: {
            float_list: {
              value: [ 4.5 ]
            }
          }
          feature: {
            float_list: {
              value: [ 5.0 ]
            }
          }
        }
      }
      feature_list: {
        key  : "movie_names"
        value: {
          feature: {
            bytes_list: {
              value: [ "The Shawshank Redemption" ]
            }
          }
          feature: {
            bytes_list: {
              value: [ "Fight Club" ]
            }
          }
        }
      }
      feature_list: {
        key  : "actors"
        value: {
          feature: {
            bytes_list: {
              value: [ "Tim Robbins", "Morgan Freeman" ]
            }
          }
          feature: {
            bytes_list: {
              value: [ "Brad Pitt", "Edward Norton", "Helena Bonham Carter" ]
            }
          }
        }
      }
    }

    A conformant SequenceExample data set obeys the following conventions:

    Context:
      - All conformant context features K must obey the same conventions as
        a conformant Example's features (see above).
    Feature lists:
      - A FeatureList L may be missing in an example; it is up to the
        parser configuration to determine if this is allowed or considered
        an empty list (zero length).
      - If a FeatureList L exists, it may be empty (zero length).
      - If a FeatureList L is non-empty, all features within the FeatureList
        must have the same data type T. Even across SequenceExamples, the type T
        of the FeatureList identified by the same key must be the same. An entry
        without any values may serve as an empty feature.
      - If a FeatureList L is non-empty, it is up to the parser configuration
        to determine if all features within the FeatureList must
        have the same size.  The same holds for this FeatureList across multiple
        examples.
      - For sequence modeling, e.g.:
           http://colah.github.io/posts/2015-08-Understanding-LSTMs/
           https://github.com/tensorflow/nmt
        the feature lists represent a sequence of frames.
        In this scenario, all FeatureLists in a SequenceExample have the same
        number of Feature messages, so that the ith element in each FeatureList
        is part of the ith frame (or time step).
    Examples of conformant and non-conformant examples' FeatureLists:

    Conformant FeatureLists:
       feature_lists: { feature_list: {
         key: "movie_ratings"
         value: { feature: { float_list: { value: [ 4.5 ] } }
                  feature: { float_list: { value: [ 5.0 ] } } }
       } }

    Non-conformant FeatureLists (mismatched types):
       feature_lists: { feature_list: {
         key: "movie_ratings"
         value: { feature: { float_list: { value: [ 4.5 ] } }
                  feature: { int64_list: { value: [ 5 ] } } }
       } }

    Conditionally conformant FeatureLists, the parser configuration determines
    if the feature sizes must match:
       feature_lists: { feature_list: {
         key: "movie_ratings"
         value: { feature: { float_list: { value: [ 4.5 ] } }
                  feature: { float_list: { value: [ 5.0, 6.0 ] } } }
       } }

    Conformant pair of SequenceExample
       feature_lists: { feature_list: {
         key: "movie_ratings"
         value: { feature: { float_list: { value: [ 4.5 ] } }
                  feature: { float_list: { value: [ 5.0 ] } } }
       } }
    and:
       feature_lists: { feature_list: {
         key: "movie_ratings"
         value: { feature: { float_list: { value: [ 4.5 ] } }
                  feature: { float_list: { value: [ 5.0 ] } }
                  feature: { float_list: { value: [ 2.0 ] } } }
       } }

    Conformant pair of SequenceExample
       feature_lists: { feature_list: {
         key: "movie_ratings"
         value: { feature: { float_list: { value: [ 4.5 ] } }
                  feature: { float_list: { value: [ 5.0 ] } } }
       } }
    and:
       feature_lists: { feature_list: {
         key: "movie_ratings"
         value: { }
       } }

    Conditionally conformant pair of SequenceExample, the parser configuration
    determines if the second feature_lists is consistent (zero-length) or
    invalid (missing "movie_ratings"):
       feature_lists: { feature_list: {
         key: "movie_ratings"
         value: { feature: { float_list: { value: [ 4.5 ] } }
                  feature: { float_list: { value: [ 5.0 ] } } }
       } }
    and:
       feature_lists: { }

    Non-conformant pair of SequenceExample (mismatched types)
       feature_lists: { feature_list: {
         key: "movie_ratings"
         value: { feature: { float_list: { value: [ 4.5 ] } }
                  feature: { float_list: { value: [ 5.0 ] } } }
       } }
    and:
       feature_lists: { feature_list: {
         key: "movie_ratings"
         value: { feature: { int64_list: { value: [ 4 ] } }
                  feature: { int64_list: { value: [ 5 ] } }
                  feature: { int64_list: { value: [ 2 ] } } }
       } }

    Conditionally conformant pair of SequenceExample; the parser configuration
    determines if the feature sizes must match:
       feature_lists: { feature_list: {
         key: "movie_ratings"
         value: { feature: { float_list: { value: [ 4.5 ] } }
                  feature: { float_list: { value: [ 5.0 ] } } }
       } }
    and:
       feature_lists: { feature_list: {
         key: "movie_ratings"
         value: { feature: { float_list: { value: [ 4.0 ] } }
                  feature: { float_list: { value: [ 5.0, 3.0 ] } }
       } }
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CONTEXT_FIELD_NUMBER: builtins.int
    FEATURE_LISTS_FIELD_NUMBER: builtins.int
    @property
    def context(self) -> tensorflow.core.example.feature_pb2.Features: ...
    @property
    def feature_lists(self) -> tensorflow.core.example.feature_pb2.FeatureLists: ...
    def __init__(
        self,
        *,
        context: tensorflow.core.example.feature_pb2.Features | None = ...,
        feature_lists: tensorflow.core.example.feature_pb2.FeatureLists | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["context", b"context", "feature_lists", b"feature_lists"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["context", b"context", "feature_lists", b"feature_lists"]) -> None: ...

global___SequenceExample = SequenceExample
